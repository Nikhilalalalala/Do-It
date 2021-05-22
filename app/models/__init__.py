# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies
# from .User import User
# from .Task import Task
# from .base import db


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# TODO Where to do input validation?

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    date_goal = db.Column(db.Date, nullable=True)

    #TODO ENSURE end_date > date_created

    def __init__(self, name: str, description: str, userid: int, date_goal: datetime = None):
        self.name = name
        self.description= description
        self.date_created = datetime.now()
        self.userid = userid
        self.date_goal = date_goal
        
    def __repr__(self) -> str:
        return f'<ID: {self.id}\nNAME: {self.name}\nDESC: {self.description}>\n'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date_joined = db.Column(db.Date, nullable=False)

    def __init__(self, name: str):
        self.name = name
        self.date_joined = datetime.now()

    def __repr__(self) -> str:
        return f'<ID: {self.id}\nNAME: {self.name}\n'
