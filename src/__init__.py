import logging
import os
from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS

from src.models import DB
from src.views import add_all_blueprints


def create_app(test_config=None):
    """生成Flask app的工厂方法

    Args:
        test_config (Mapping[str, Any], optional): 配置文件. Defaults to None.

    Returns:
        Flask: 生成的Flask App
    """

    # 创建并配置app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # Flask 密钥
        SQLALCHEMY_DATABASE_URI="postgresql://scheduler:123456@localhost:5432/scheduler",
        REMEMBER_COOKIE_SAMESITE="None",
        REMEMBER_COOKIE_SECURE=True,
        INVITATION_CODE="invitation",
    )

    # 开启跨源支持
    CORS(app, supports_credentials=True)

    # 加载实例配置
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化数据库
    DB.init_app(app)
    with app.app_context():
        DB.create_all()

    # 添加蓝图
    add_all_blueprints(app)

    # 开启日志
    root = logging.getLogger()
    root.addHandler(default_handler)

    return app
