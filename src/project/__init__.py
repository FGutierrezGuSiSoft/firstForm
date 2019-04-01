from flask import Flask
from flask_cors import CORS


def register_blueprints(app):
    from project.views.pages import pages_blueprint

    app.register_blueprint(pages_blueprint)


def create_app(script_info=None):
    app = Flask(__name__, static_folder='public', static_url_path='')

    CORS(app)

    app.config.from_object('project.config.BaseConfig')

    register_blueprints(app)

    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app
