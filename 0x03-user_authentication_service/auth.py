#!/usr/bin/env python3
'''
Auth module
'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    hash password
    '''
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        '''
        initialize
        '''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        register user
        '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hass_pass = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hass_pass)
            return user
        raise ValueError(f"User {email} already exists")
