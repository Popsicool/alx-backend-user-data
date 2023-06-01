#!/usr/bin/env python3
'''
Session auth
'''
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    '''
    session db
    '''
    def create_session(self, user_id=None):
        '''
        overide create session
        '''
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        ags = {
            "user_id": user_id,
            "session_id": session_id
        }
        user = UserSession(**ags)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        user id
        """
        user = UserSession.search({"session_id": session_id})
        if user:
            return user
        return None

    def destroy_session(self, request=None):
        """
        destroy session
        """
        if request is None:
            return False
        session = self.session_cookie(request)
        if not session:
            return False
        user_ses = UserSession.search({"session_id": session})
        if user_ses:
            user_ses[0].remove()
            return True
        return False
