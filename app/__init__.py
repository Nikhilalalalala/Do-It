from flask import Flask, request, Blueprint
from flask_restful import Api
from .resources import Users, Tasks, Auth, UserDetails, Base
import os

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

# Route
api.add_resource(Base, '/')
api.add_resource(Users, '/users')
api.add_resource(UserDetails, '/userdetails')
api.add_resource(Tasks, '/tasks')
# api.add_resource(TaskList, '/tasks/<userid>')
api.add_resource(Auth, "/auth")