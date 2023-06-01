#!/usr/bin/env python3
'''
Session Auth with expiring
'''
from .session_auth import SessionAuth
import uuid
import base64
from typing import Tuple, TypeVar
from models.user import User
from os import getenv
from datetime import datetime


class SessionExpAuth(SessionAuth):
    '''
    session that expire
    '''
    def __init__(self):
        '''
        initialize
        '''
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except BaseException:
            self.session_duration = 0

    def create_session(self, user_id=None):
        '''
        overwrite create session
        '''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id, "created_at": datetime.now()}
        return session_id
