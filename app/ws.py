from flask import Flask
from app.views import index, getkeyz

def create_app(config_object=None):
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(getkeyz.blueprint)
    app.register_blueprint(index.blueprint)

