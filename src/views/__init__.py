import logging
from flask import Flask

from .user import user_blueprint, login_manager

logger = logging.getLogger("views")


def add_all_blueprints(app: Flask):
    login_manager.init_app(app)
    app.register_blueprint(user_blueprint)
