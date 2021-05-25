from sqlalchemy import exc
from app.models import db, Task, User
import uuid

class DBService():
    @staticmethod
    def addObjectIntoDB(item):
        try: 
            db.session.add(item)
            db.session.commit()
        
            return True
        except exc.SQLAlchemyError as e:
            print(e)
            return False

    @staticmethod
    def addUser(name, email, hashed_password):
        user = User(name, email, hashed_password)
        return DBService.addObjectIntoDB(user)
    
    @staticmethod
    def addTask(name, desc, userid, date_goal):
        task = Task(name, desc, userid, date_goal)
        return DBService.addObjectIntoDB(task)

    @staticmethod
    def getTasksFromUser(userid):
        print(userid)
        return Task.query.filter_by(userid=userid)

    @staticmethod
    def getUserByUsername(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def getUserByID(id):
        return User.query.filter_by(id=id).first()
        
        
