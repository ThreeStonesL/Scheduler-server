from datetime import datetime
import logging
from .database import DB, Folder

logger = logging.getLogger("models.folder")
logger.setLevel(level=logging.DEBUG)


def add_folder_info(
    id: int,
    name: str,
    modifiedTime: datetime,
    userId: int,
    order: int,
    icon: str | None = None,
    color: str | None = None,
):
    folder = Folder(
        id=id,
        name=name,
        modifiedTime=modifiedTime,
        userId=userId,
        icon=icon,
        order=order,
        color=color,
    )
    try:
        DB.session.add(folder)
        DB.session.commit()
        logger.debug(f"\nAdd folder: {folder}")
        return True
    except Exception as e:
        logger.warning(f"\nAdd folder: \n{e}")
        return False


def add_folder_infos():
    # TODO: 批量添加folder
    pass


def remove_folder_info(id: int):
    # TODO: 添加folder
    pass
