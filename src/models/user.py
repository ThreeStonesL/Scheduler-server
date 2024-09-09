import logging
from sqlalchemy.exc import IntegrityError, NoResultFound

from .database import DB, User


logger = logging.getLogger("models.user")
logger.setLevel(level=logging.DEBUG)


def add_user_info(email: str, username: str, password: bytes) -> int | None:
    user = User(email=email, username=username, password=password)
    try:
        DB.session.add(user)
        DB.session.commit()
        logger.debug(f"\nAdd User: {user}")
        return user.id
    except IntegrityError:
        return None


def get_user_info_by_id(user_id):
    try:
        return DB.session.query(User).where(User.id == user_id).one()
    except NoResultFound:
        return None


def get_user_info_by_email(email):
    try:
        return DB.session.query(User).where(User.email == email).one()
    except NoResultFound:
        return None


def remove_user_info(user_id):
    try:
        DB.session.query(User).where(User.id == user_id).delete()
        DB.session.commit()
        logger.debug(f"\nremove user: {{ userId={user_id} }}")
        return True
    except NoResultFound:
        return False
