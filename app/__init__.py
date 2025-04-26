from flask import Flask
from config import config

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    environment = 'production'
    app.config.from_object(config[environment])

    from app.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
