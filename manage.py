import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from run import app
from app.models import db

load_dotenv()
database_url = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()