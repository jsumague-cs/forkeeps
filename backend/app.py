# app.py
from flask import Flask, request, jsonify
from config import Config
from models import db, migrate, User, Couple, DateIdea, Date, Memory

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions with app
db.init_app(app)
migrate.init_app(app, db)

# --- ROUTES ---

@app.route('/')
def home():
    return jsonify({"message": "Forkeeps API is running!"})

@app.route('/health', methods=['GET'])
def health_check():
    try:
        db.session.execute(db.select(1))
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Create users then create a couple space for them
@app.route('/api/users', methods=['POST'])
def create_user():
    create_user = request.get_json() or {}
    username = create_user.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Account created successfully!", "user_id": new_user.id, "username": new_user.username}), 201 


@app.route('/api/couples', methods=['POST'])
def create_couple():
    data = request.get_json() or {}
    
    # Requires two user IDs
    user1_id = data.get('user1_id')
    user2_id = data.get('user2_id')

    if not user1_id or not user2_id:
        return jsonify({"error": "user1_id and user2_id are required"}), 400
    
    if user1_id == user2_id:
        return jsonify({"error": "invalid request"}), 400
    
    
    user1 = User.query.get(user1_id)
    user2 = User.query.get(user2_id)

    if not user1 or not user2:
        return jsonify({"error": "user does not exist"}), 404
    
    new_couple = Couple(user1_id=user1_id, user2_id=user2_id)
    db.session.add(new_couple)
    db.session.commit()
    
    return jsonify({"message": "Couple space created!", "couple_id": new_couple.id}), 201

# Get all Date Ideas for a couple
@app.route('/api/couples/<int:couple_id>/ideas', methods=['GET'])
def get_date_ideas(couple_id):

    couple = Couple.query.get(couple_id)
    
    if not couple:
        return jsonify({"error": "Couple not found"}), 404

    
    ideas = DateIdea.query.filter_by(couple_id=couple_id).all()
    results = [
        {
            "id": idea.id,
            "title": idea.title,
            "description": idea.description,
            "category": idea.category,
            "estimated_budget": float(idea.estimated_budget) if idea.estimated_budget else 0.0,
            "status": idea.status,
            "scheduled_date": idea.scheduled_date.isoformat() if idea.scheduled_date else None,
            "created_at": idea.created_at.isoformat() if idea.created_at else None

        }
        for idea in ideas
    ]
    return jsonify(results), 200

# Add a new Date Idea
@app.route('/api/couples/<int:couple_id>/ideas', methods=['POST'])
def add_date_idea(couple_id):
    data = request.get_json()

    couple = Couple.query.get(couple_id)

    if not couple:
        return jsonify({"error": "Couple not found"}), 404
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    new_idea = DateIdea(
        couple_id=couple_id,
        title=data['title'],
        description=data.get('description', ''),
        category=data.get('category', 'General'),
        estimated_budget=data.get('estimated_budget', 0.0),
        status=data.get('status', 'idea'),
        scheduled_date=data.get('scheduled_date', None)
    )
    
    db.session.add(new_idea)
    db.session.commit()
    
    return jsonify({"message": "Date idea created successfully!", "id": new_idea.id}), 201

# Add a Date endpoint
@app.route('/api/couples/<int:couple_id>/dates', methods=['POST'])
def add_date(couple_id):
    data = request.get_json()

    couple = Couple.query.get(couple_id)

    if not couple:
        return jsonify({"error": "Couple not found"}), 404
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    dateidea_id = data.get('dateidea_id')

    if dateidea_id:
        idea = DateIdea.query.filter_by(id=dateidea_id, couple_id=couple_id).first()
        if not idea:
            return jsonify({"error": "Date idea not found for this couple"}), 404
    
    new_date = Date(
        couple_id=couple_id,
        title=data['title'],
        description=data.get('description', ''),
        category=data.get('category', 'General'),
        budget=data.get('budget', 0.0),
        status=data.get('status', 'planned'),
        scheduled_at=data.get('scheduled_at', None),
        location=data.get('location', '')
    )
    
    db.session.add(new_date)
    db.session.commit()
    
    return jsonify({"message": "Date created successfully!", "id": new_date.id}), 201
@app.route('/api/couples/<int:couple_id>/dates', methods=['GET'])
def get_dates(couple_id):
    couple = Couple.query.get(couple_id)

    if not couple:
        return jsonify({"error": "Couple not found"}), 404

    dates = Date.query.filter_by(couple_id=couple_id).all()
    results = [
        {
            "id": date.id,
            "title": date.title,
            "description": date.description,
            "category": date.category,
            "budget": float(date.budget) if date.budget else 0.0,
            "status": date.status,
            "scheduled_at": date.scheduled_at.isoformat() if date.scheduled_at else None,
            "location": date.location,
            "created_at": date.created_at.isoformat() if date.created_at else None

        }
        for date in dates
    ]
    return jsonify(results), 200

@app.route('/api/couples/<int:couple_id>/dates/<int:date_id>/memory', methods=['GET'])
def get_memory(couple_id, date_id):

    couple = Couple.query.get(couple_id)

    if not couple:
        return jsonify({"error": "Couple not found"}), 404

    date = Date.query.filter_by(id=date_id, couple_id=couple_id).first()

    if not date:
        return jsonify({"error": "Date not found"}), 404

    memory = Memory.query.filter_by(date_id=date.id).first()

    if not memory:
        return jsonify({"error": "Memory not found for this date"}), 404

    result = {
        "id": memory.id,
        "date_id": memory.date_id,
        'title': memory.title,
        'journal_entry': memory.journal_entry,
        'actual_expense': memory.actual_expense,
        'location': memory.location,
        'rating': memory.rating,
        "created_at": memory.created_at.isoformat() if memory.created_at else None
    }
    return jsonify(result), 200

@app.route('/api/couples/<int:couple_id>/dates/<int:date_id>/memory', methods=['POST'])
def add_memory(couple_id, date_id):
    data = request.get_json()

    couple = Couple.query.get(couple_id)

    if not couple:
        return jsonify({"error": "Couple not found"}), 404

    memory = Date.query.filter_by(id=date_id, couple_id=couple_id).first()

    if memory:
        return jsonify("error":"Memory already exists for this date."), 400
    
    if not memory:
        return jsonify({"error": "Date not found"}), 404

    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    new_memory = Memory(
        date_id=date.id,
        title=data['title'],
        journal_entry=data.get('journal_entry', ''),
        actual_expense=data.get('actual_expense', 0.0),
        location=data.get('location', ''),
        rating=data.get('rating', None)
    )
    
    db.session.add(new_memory)
    db.session.commit()
    
    return jsonify({"message": "Memory created successfully!", "id": new_memory.id}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)