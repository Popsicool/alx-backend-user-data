#!/usr/bin/env python3
"""
class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    '''
    class Auth
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth
        """
        if path is None or excluded_paths is None or len(excluded_paths) < 1:
            return True
        if (path + "/") in excluded_paths:
            return False
        for p in excluded_paths:
            if p.startswith(path):
                return False
            if path.startswith(p):
                return False
            if p[-1] == "*":
                if path.startswith(p[:-1]):
                    return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        '''
        authorization header
        '''
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current user
        '''
        return None
