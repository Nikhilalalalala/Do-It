from flask import Flask
from app import api_bp
from app.models import db

app = Flask(__name__)

def configure_app(config_filename):
    app.config.from_object(config_filename)
    
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)
    
    return app

app = configure_app("config")
app.run(debug=True)

# if __name__ == "__main__":
#     app = configure_app("config")
#     app.run(debug=True)
# app = configure_app("config")
# application = app
# application.run()