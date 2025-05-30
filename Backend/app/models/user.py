# backend/src/models/user.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    oauth_id = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False, default='customer')
