# backend/app.py
from flask import Flask, request, jsonify
from config import Config
from models import db, Couple, DateIdea, Memory

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with Flask
db.init_app(app)

# Create database tables automatically upon startup
with app.app_context():
    db.create_all()

# --- ROUTES ---

@app.route('/')
def home():
    return jsonify({"message": "Forkeeps API is running!"})

# Health Check Route
@app.route('/health', methods=['GET'])
def health_check():
    try:
        db.session.execute(db.select(1))
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Create a demo shared couple space (Helper endpoint)
@app.route('/api/couples', methods=['POST'])
def create_couple():
    new_couple = Couple()
    db.session.add(new_couple)
    db.session.commit()
    return jsonify({"message": "Couple space created!", "couple_id": new_couple.id}), 201

# Get all Date Ideas for a couple
@app.route('/api/couples/<int:couple_id>/ideas', methods=['GET'])
def get_date_ideas(couple_id):
    ideas = DateIdea.query.filter_by(couple_id=couple_id).all()
    results = [
        {
            "id": idea.id,
            "title": idea.title,
            "description": idea.description,
            "category": idea.category,
            "estimated_budget": float(idea.estimated_budget) if idea.estimated_budget else 0.0,
            "status": idea.status
        }
        for idea in ideas
    ]
    return jsonify(results), 200

# Add a new Date Idea
@app.route('/api/couples/<int:couple_id>/ideas', methods=['POST'])
def add_date_idea(couple_id):
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    new_idea = DateIdea(
        couple_id=couple_id,
        title=data['title'],
        description=data.get('description', ''),
        category=data.get('category', 'General'),
        estimated_budget=data.get('estimated_budget', 0.0),
        status='idea'
    )
    
    db.session.add(new_idea)
    db.session.commit()
    
    return jsonify({"message": "Date idea created successfully!", "id": new_idea.id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)