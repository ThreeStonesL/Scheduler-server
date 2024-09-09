import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode("utf-8"), hashed_password)
