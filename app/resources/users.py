from flask.json import jsonify
from werkzeug.security import generate_password_hash
from flask_restful import Resource
from app.dbservice import DBService
from flask import request
import json


class Users(Resource):

    def post(self):
        # Create new user
        body = json.loads(request.data)
        username = body['username']
        email = body['email']
        password = body['password']
        hashed_password = generate_password_hash(password, method='sha256')

        result = DBService.addUser(username, email, hashed_password)
        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400