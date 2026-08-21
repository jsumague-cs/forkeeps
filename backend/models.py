# backend/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# 1. Add User
class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    date_ideas = db.relationship('DateIdea', backref='user', lazy=True)
    date = db.relationship('Date', backref='user', lazy=True)
    memories = db.relationship('Memory', backref='user', lazy=True)
    photos = db.relationship('Photos', backref='user', lazy=True)
    

# 2. Date Ideas & Planned Dates
class DateIdea(db.Model):
    __tablename__ = 'date_ideas'

    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couples.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    estimated_budget = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(db.String(20), default="idea")  # 'idea', 'planned', 'completed'
    scheduled_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


#date mismo
class Date(db.Model):
    __tablename__ = 'date'

    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couples.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    estimated_budget = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(db.String(20), default="idea")  # 'idea', 'planned', 'completed'
    scheduled_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# 3. Completed Date Memories
class Memory(db.Model):
    __tablename__ = 'memories'

    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couples.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    journal_entry = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    actual_expense = db.Column(db.Numeric(10, 2), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

#data for photos
class Photos(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    memory_id = db.Column(db.Integer, db.ForeignKey('memories.id'), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)