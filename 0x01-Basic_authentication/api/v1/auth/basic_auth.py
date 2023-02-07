#!/usr/bin/env python3
"""Basic Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        auth = authorization_header.split(' ')
        if len(auth) != 2 or auth[0] != 'Basic':
            return None
        return auth[1]
