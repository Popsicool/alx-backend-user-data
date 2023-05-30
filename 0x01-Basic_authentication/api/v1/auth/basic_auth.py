#!/usr/bin/env python3
'''
Basic Auth module
'''
from .auth import Auth


class BasicAuth(Auth):
    '''
     class BasicAuth that inherits from Auth
     '''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extracts base64 from header
        """
        if authorization_header is None or not isinstance(
                authorization_header,
                str) or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]
