#!/usr/bin/env python3
"""
user session
"""
from models.base import Base


class UserSession(Base):
    '''
    user session
    '''
    def __init__(self, *args: list, **kwargs: dict):
        '''
        init
        '''
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
