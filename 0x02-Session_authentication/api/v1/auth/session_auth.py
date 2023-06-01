#!/usr/bin/env python3
'''
Session Auth module
'''
from .auth import Auth
import uuid
import base64
from typing import Tuple, TypeVar
from models.user import User


class SessionAuth(Auth):
    '''
     class BasicAuth that inherits from Auth
     '''

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        create session for user
        '''
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        returns a user id from session
        '''
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''
        return current user
        '''
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        user = User.get(user_id)
        if user:
            return user.to_json()

        return None

    def destroy_session(self, request=None):
        '''
        logout user by deleting session
        '''
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
