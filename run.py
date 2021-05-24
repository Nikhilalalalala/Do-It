from flask import Flask

app = Flask(__name__)

def configure_app(config_filename):
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = configure_app("config")
    app.run(debug=True)