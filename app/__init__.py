from flask import Flask, request, Blueprint
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from dotenv import load_dotenv
from flask_restful import Api
# from app.models import db
from .resources import Users, Tasks, Auth
import os

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Users, '/users')
api.add_resource(Tasks, '/tasks')
# api.add_resource(TaskList, '/tasks/<userid>')
api.add_resource(Auth, "/auth")