import logging
from flask import Flask

from .user import user_blueprint, login_manager
from .folder import folder_blueprint

logger = logging.getLogger("views")


def add_all_blueprints(app: Flask):
    login_manager.init_app(app)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(folder_blueprint)
