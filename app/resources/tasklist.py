from app.dbservice import DBService
from flask_restful import Resource, abort
from flask import request
from .auth import token_required
import json

# class TaskList(Resource):

#     @token_required
#     def get(current_user):
#         """
#         Get all tasks from userid
#         """
#         if not userid:
#             return { "status": 'error' , 'error': 'No userid provided'}, 400
#         else:
#             tasklist = DBService.getTasksFromUser(userid)
#             if not tasklist:
#                 # no tasks found for the user
#                 return { "status": 'success', "tasks": "" }, 200
#             else:
#                 all_tasks = []
#                 for task in tasklist:
#                     task = task.__dict__
#                     task_data = {
#                         'id': task['id'],
#                         'userid': task['id'],
#                         'name': task['name'],
#                         'description': task['description'],
#                     }
#                     if task['date_created'] is not None:
#                         task_data['date_created'] = task['date_created'].strftime("%m/%d/%Y, %H:%M:%S"),
#                     if task['date_goal'] is not None:
#                         task_data['date_goal'] = task['date_goal'].strftime("%m/%d/%Y, %H:%M:%S")

#                     all_tasks.append(task_data)

#                 json_string = json.dumps([all_tasks])
#                 return { "status": 'success', "tasks": json_string }, 200


