import logging
from flask import Blueprint, current_app, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from src.models.user import (
    add_user_info,
    get_user_info_by_email,
    get_user_info_by_id,
    remove_user_info,
)
from src.utils.password import check_password, hash_password
from src.views.forms import DeleteForm, LoginForm, RegisterForm


user_blueprint = Blueprint("user", __name__, url_prefix="/user")
login_manager = LoginManager()
logger = logging.getLogger("views.user")
logger.setLevel(level=logging.DEBUG)


class User:
    def __init__(self, id, email, username) -> None:
        self.id = str(id)
        self.email = email
        self.username = username
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    user_info = get_user_info_by_id(user_id)
    if user_info:
        return User(
            user_info.id,
            user_info.email,
            user_info.username,
        )
    else:
        return None


@user_blueprint.route("/register", methods=["POST"])
def register():
    form = RegisterForm(request.form)
    if not form.validate():
        return ({"errors": form.errors}, 400)

    if request.form.get("invitation") != current_app.config["INVITATION_CODE"]:
        return ({"error": "invalid invitation code"}, 400)

    result = add_user_info(
        email=request.form["email"],
        username=request.form["username"],
        password=hash_password(request.form["password"]),
    )
    if not result:
        return ({"error": "The email is already in use"}, 400)

    return {
        "username": request.form["username"],
        "email": request.form["email"],
        "id": result,
    }


@user_blueprint.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)

    if not form.validate():
        return ({"errors": form.errors}, 400)

    # 查找对应用户
    user_info = get_user_info_by_email(request.form["email"])

    if not user_info:
        return ({"error": "No such user"}, 400)
    if not check_password(user_info.password, request.form["password"]):
        return ({"error": "Wrong password"}, 400)

    login_user(
        User(
            user_info.id,
            user_info.email,
            user_info.username,
        ),
        remember=(request.form.get("remember", default="") == "remember"),
    )
    return {
        "username": user_info.username,
        "email": user_info.email,
        "id": user_info.id,
    }


@user_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    # TODO: 前端待实现
    logout_user()
    return {"message": "Successful"}


@user_blueprint.route("/delete", methods=["DELETE"])
@login_required
def delete():
    # TODO: 前端待实现
    # 表单验证
    form = DeleteForm(request.form)
    if not form.validate():
        return ({"errors": form.errors}, 400)

    user_info = get_user_info_by_id(request.form["id"])

    # 判断是否存在对应user
    if not user_info:
        return ({"error": "No such user"}, 400)

    # 判断对应email是否正确
    if user_info.email != request.form["email"]:
        return ({"error": "Email is wrong"}, 400)

    # 判断username是否正确
    if user_info.username != request.form["username"]:
        return ({"error": "Username is wrong"}, 400)

    # 判断密码是否正确
    if not check_password(user_info.password, request.form["password"]):
        return ({"error": "Wrong password"}, 400)

    result = remove_user_info(request.form["id"])
    if result:
        logout_user()
        return {"message": "success"}
    else:
        return ({"error": "Unknown Error"}, 400)


@user_blueprint.route("/check", methods=["GET"])
@login_required
def check():
    return {
        "username": current_user.username,
        "id": current_user.id,
        "email": current_user.email,
    }


@user_blueprint.route("/change_password", methods=["POST"])
@login_required
def change_password():
    # TODO: 修改密码
    return ({"error": "developing"}, 400)
