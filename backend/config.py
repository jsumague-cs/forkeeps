import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:gileanne1122@localhost:5432/forkeeps_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False