from flask import Flask
from app import api_bp
from app.models import db
import os

app = Flask(__name__)

def configure_app(config_filename):
    # try:
    #     app.config.from_object(config_filename)
    # except ModuleNotFoundError:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
        # app.config['SQLALCHEMY_ECHO'] = os.environ['SQLALCHEMY_ECHO']

    
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)
    
    return app

# app = configure_app("config")
# app.run(debug=True)

if __name__ == "__main__":
    app = configure_app("config")
    app.run(debug=True)
# app = configure_app("config")
# application = app
# application.run()