from app.models import User
from app.resources.auth import token_required
from app.dbservice import DBService
from flask_restful import Resource
from flask import request
import json

class Tasks(Resource):
    @token_required
    def post(current_user:User, self):
        # Adding a task
        userid = current_user.getId()
        data = json.loads(request.data)
        result = DBService.addTask(data, userid)

        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400

    
    @token_required
    def put(current_user, self):
        userid = current_user.getId()
        if not userid:
            return { "status": 'error' , 'error': 'No userid provided'}, 400
        else:
            data = json.loads(request.data)
            userid = current_user.getId()
            result = DBService.updateTask(data, userid)
            print(result)
            if result:     
                return { "status": 'success' }, 200
            else:
                return { "status": 'error' }, 400
            
    @token_required
    def delete(current_user, self):
        userid = current_user.getId()
        data = json.loads(request.data)
        print(data)
        if data['id'] != None:
            result = DBService.deleteTaskById(data['id'])
            if result: 
                return { "status": 'success' }, 
        return { "status": 'error' }, 400

    @token_required
    def get(current_user, self):
        """
        Get all tasks from userid
        """        
        userid = current_user.getId()
        if not userid:
            return { "status": 'error' , 'error': 'No userid provided'}, 400
        else:
            tasklist = DBService.getTasksFromUser(userid)
            if not tasklist:
                # no tasks found for the user
                return { "status": 'success', "tasks": "" }, 200
            else:
                all_tasks = []
                for task in tasklist:
                    task = task.__dict__
                    
                    task_data = {
                        'id': task['id'],
                        'userid': task['id'],
                        'name': task['name'],
                        'description': task['description'],
                        'isDone' : task['isDone'],
                        # 'dateGoal': task['date_goal']
                    }
                    if task['date_created'] is not None:
                        task_data['date_created'] = task['date_created'].strftime("%Y-%m-%d %H:%M:%S"),
                    if task['date_goal'] is not None:
                        task_data['date_goal'] = task['date_goal'].strftime("%Y-%m-%d %H:%M:%S")
                    
                    all_tasks.append(task_data)

                json_string = json.dumps(all_tasks)
                return { "status": 'success', "tasks": json_string }, 200
