from .base import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    
    def __init__(self, name):
        self.name = name
