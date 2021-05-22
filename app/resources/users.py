from flask_restful import Resource
from app.dbservice import DBService
from flask import request

class Users(Resource):

    def get(self):
        return {"message": "Hello, World!"}

    def post(self):
        # Adding a task
        name = request.json['name']

        result = DBService.addUser(self, name)
        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400