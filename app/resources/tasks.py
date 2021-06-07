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
        data = json.loads(request.data)
        name = data['name']
        description = data['description']
        date_goal = None
        if "date_goal" in data:
            date_goal = data['date_goal']
        userid = current_user.getId()
        
        result = DBService.addTask(name, description, userid, date_goal)

        if result:     
            return { "status": 'success' }, 200
        else:
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
            print(tasklist.__dir__)
            print(tasklist)
            if not tasklist:
                # no tasks found for the user
                return { "status": 'success', "tasks": "" }, 200
                
            # if len(tasklist) == 0:
            #     # no tasks found for the user
            #     return { "status": 'success', "tasks": "" }, 200
            else:
                all_tasks = []
                for task in tasklist:
                    task = task.__dict__
                    task_data = {
                        'id': task['id'],
                        'userid': task['id'],
                        'name': task['name'],
                        'description': task['description'],
                        # 'isDone' : task['isDone'],
                    }
                    if task['date_created'] is not None:
                        task_data['date_created'] = task['date_created'].strftime("%m/%d/%Y, %H:%M:%S"),
                    if task['date_goal'] is not None:
                        task_data['date_goal'] = task['date_goal'].strftime("%m/%d/%Y, %H:%M:%S")

                    all_tasks.append(task_data)

                json_string = json.dumps(all_tasks)
                print(json_string)
                return { "status": 'success', "tasks": json_string }, 200
