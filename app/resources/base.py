from flask_restful import Resource

class Base(Resource):

    def get(self):
        return "App is running"