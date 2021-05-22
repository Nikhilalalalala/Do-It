from app import dbservice
from flask_restful import Resource
from flask import request

class Tasks(Resource):
    def post(self):
        # Adding a task
        name = request.json['name']
        description = request.json['description']
        userid = request.json['userid']

        result = dbservice.DBService.addTask(self, name, description, userid)
        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400
