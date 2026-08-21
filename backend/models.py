# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# 1. Users & Couples
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Couple(db.Model):
    __tablename__ = 'couples'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user1 = db.relationship('User', foreign_keys=[user1_id], backref='couples_as_user1')
    user2 = db.relationship('User', foreign_keys=[user2_id], backref='couples_as_user2')

    date_ideas = db.relationship('DateIdea', backref='couple', lazy=True)
    dates = db.relationship('Date', backref='couple', lazy=True)


# 2. Date Ideas & Planned Dates
class DateIdea(db.Model):
    __tablename__ = 'date_ideas'

    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couples.id'), nullable=False)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    estimated_budget = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(db.String(50), default='idea')  # Added status field
    scheduled_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    dates = db.relationship('Date', backref='date_idea', lazy=True)


class Date(db.Model):
    __tablename__ = 'dates'

    id = db.Column(db.Integer, primary_key=True)
    couple_id = db.Column(db.Integer, db.ForeignKey('couples.id'), nullable=False)
    dateidea_id = db.Column(db.Integer, db.ForeignKey('date_ideas.id'), nullable=True)

    title = db.Column(db.String(150), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(50), nullable=True)
    budget = db.Column(db.Numeric(10, 2), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    memory = db.relationship('Memory', backref='date', lazy=True, uselist=False)


# 3. Completed Date Memories & Photos
class Memory(db.Model):
    __tablename__ = 'memories'

    id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    journal_entry = db.Column(db.Text, nullable=True)
    actual_expense = db.Column(db.Numeric(10, 2), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    photos = db.relationship('Photo', backref='memory', lazy=True)


class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    memory_id = db.Column(db.Integer, db.ForeignKey('memories.id'), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)