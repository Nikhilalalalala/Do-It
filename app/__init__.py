from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.models import db, User, Task
import os

app = Flask(__name__)

def start_app():
    # load environment variables
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize Flask SQLALchemy with this flask app
    db.init_app(app)

    return app

@app.route('/')
def start():
    return "Start Now!"

@app.route('/addTask', methods=["POST"])
def addTask():
    name = request.json['name']
    description = request.json['description']
    userid = request.json['userid']

    new_task = Task(name, description, userid)
    
    db.session.add(new_task)
    db.session.commit()
    
    return "adding task"


@app.route('/addUser', methods=["POST"])
def addUser():
    name = request.json['name']

    new_user = User(name)
    
    db.session.add(new_user)
    db.session.commit()
    
    return "adding user"