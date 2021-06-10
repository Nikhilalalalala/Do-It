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
    def addUser(name, email, hashed_password):
        user = User(name, email, hashed_password)
        return DBService.addObjectIntoDB(user)
    
    @staticmethod
    def addTask(data, userid):
        name = data['name']
        description = data['description']
        date_goal = None
        if "date_goal" in data:
            date_goal = data['date_goal']
        task = Task(name, description, userid, date_goal)
        print(task)
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
        
    @staticmethod
    def getTaskById(id):
        return Task.query.filter_by(id=id).first()

    @staticmethod
    def updateTask(data, userid):
        oldTask = DBService.getTaskById(data['id'])
        # if oldTask.userid != data['id']:
        #     return False
        id = data['id']
        name = data['name']
        description = data['description']
        date_goal = None
        if "date_goal" in data:
            date_goal = data['date_goal']
        isDone = data['isDone'] == "true"
        newTask = Task(name, description, userid, date_goal, isDone)
        newDict = newTask.__dict__
        newDict.pop("_sa_instance_state")
        result = db.session.query(Task).filter(Task.id==id).update(newDict)
        db.session.commit()
        print(result)
        return result
            
    @staticmethod
    def deleteTaskById(id):
        deleteTask = Task.query.filter_by(id=id).first()
        db.session.delete(deleteTask)
        db.session.commit()
        return True
        
