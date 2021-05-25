from flask.json import jsonify
from app.dbservice import DBService
from flask.globals import request
from flask.helpers import make_response
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from run import app
from functools import wraps

class Auth(Resource):

    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response("Not authenticated", 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
        
        user = DBService.getUserByUsername(auth.username)

        #! how to determine what secrets to use 

        if check_password_hash(user.hashed_password, auth.password):
            token = jwt.encode({'id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)}, "secret", algorithm="HS512")

            return {'token' : token}
        
        return make_response("Invalid Credentials", 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

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
