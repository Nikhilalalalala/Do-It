from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from app.models import db
import os

app = Flask(__name__)

# load environment variables
load_dotenv()
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db.init_app(app)  # initialize Flask SQLALchemy with this flask app
# Migrate(app, db)

@app.route('/')
def start():
    return "Start Now!"
