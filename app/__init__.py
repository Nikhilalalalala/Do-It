from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.models import *
import os

app = Flask(__name__)

def start_app():
    # load environment variables
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize Flask SQLALchemy with this flask app
    db.init_app(app)

    return app

@app.route('/')
def start():
    return "Start Now!"

# Testing the connection with DB
@app.route('/addTask', methods=["GET"])
def addTask():
    newTask = Task(name="RANDOM")
    db.session.add(newTask)
    db.session.commit()
    return "adding task"