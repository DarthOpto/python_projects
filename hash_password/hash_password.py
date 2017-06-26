import hashlib
import uuid


def hash_password(password=None):
    """
    Hash a password
    :param password: A string password to be hashed
    :return: a hashed password
    """
    pwd = password.encode('ascii')
    salt = uuid.uuid4().hex
    hashed_pwd = hashlib.sha512(pwd + salt).hexdigest()
    print(hashed_pwd)


hash_password(password="Digitalguardian!1")