from flask_restful import Resource
from app.models import User
from app.dbservice import DBService
from flask import request
from app.resources.auth import token_required
import json

class UserDetails(Resource):

    @token_required
    def post(current_user: User, self):
        # updating bio
        userid = current_user.getId()
        body = json.loads(request.data)
        bio = body['bio']
        result = DBService.updateBioByUserid(userid, bio)
        if result:     
            return { "status": 'success' }, 200
        else:
            return { "status": 'error' }, 400

    @token_required
    def get(current_user, self):
        userid = current_user.getId()
        if not userid:
            return { "status": 'error' , 'error': 'No userid provided'}, 400
        user = DBService.getUserByID(userid)
        if not user:
            return { "status": 'error' , 'error': 'No userid provided'}, 400
        
        user_dict = user.__dict__
        return { "status": 'success', "username": user_dict['username'], "bio": user_dict['bio'] }, 200