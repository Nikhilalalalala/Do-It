from sqlalchemy import exc
from app.models import db, Task, User

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
    def addUser(self, name):
        user = User(name)
        return DBService.addObjectIntoDB(user)
    
    @staticmethod
    def addTask(self, name, desc, userid):
        task = Task(name, desc, userid)
        return DBService.addObjectIntoDB(task)
