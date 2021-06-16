from app.dbservice import DBService
from flask.globals import request
from flask_restful import Resource
from werkzeug.security import check_password_hash
import datetime
import jwt
from functools import wraps
import json 

class Auth(Resource):

    def post(self):

        auth = json.loads(request.data)

        if not auth:
           return {"status": "error", "error": "Empty body"}, 400

        auth_username = auth['username']
        auth_password =  auth['password']

        if not auth_username or not auth_password:
           return {"status": "error", "error": "Fields not given"}, 400

        user = DBService.getUserByUsername(auth_username)

        #! how to determine what secrets to use 
        if not user:
            return {"status": "error", "error": "No such user found"}, 400


        if check_password_hash(user.hashed_password, auth_password):
            token = jwt.encode({'id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)}, "secret", algorithm="HS512")

            return {'token' : token} , 200
        
        return {"status": "error", "error": "Invalid Credentials"}, 400
        
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            print("Token: ", token)

        if not token:
            return {'message' : 'Token is missing!'}, 401
        
        try: 
            data = jwt.decode(token, "secret", algorithms="HS512")
            print("\nJWT Decoded: ", data , data['id'])
            current_user = DBService.getUserByID(data['id'])
        except:
            return {'message' : 'Token is invalid!'}, 401

        return f(current_user, *args, **kwargs)

    return decorated
