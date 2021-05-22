from flask.json import jsonify
from flask_restful import Resource
from app.dbservice import DBService
from flask import request
import json

class Users(Resource):

    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        # Adding a task
        body = json.loads(request.data)
        name = body['name']

        result = DBService.addUser(self, name)
        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400