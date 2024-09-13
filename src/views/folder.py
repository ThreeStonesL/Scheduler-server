import logging
from flask import Blueprint
from flask_login import login_required

folder_blueprint = Blueprint("folder", __name__, url_prefix="/folder")
logger = logging.getLogger("views.folder")
logger.setLevel(level=logging.DEBUG)


@folder_blueprint.route("/", methods=["GET"])
@login_required
def get_folders():
    return {"message": "Unimplemented"}


@folder_blueprint.route("/", methods=["POST"])
@login_required
def add_folders():
    return {"message": "Unimplemented"}


@folder_blueprint.route("/", methods=["DELETE"])
@login_required
def delete_folders():
    return {"message": "Unimplemented"}


@folder_blueprint.route("/", methods=["PUT"])
@login_required
def change_folders():
    return {"message": "Unimplemented"}
