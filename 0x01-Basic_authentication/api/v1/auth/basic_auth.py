#!/usr/bin/env python3
"""Basic Auth"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the base64 decoded auth value"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        auth = authorization_header.split(' ')
        if len(auth) != 2 or auth[0] != 'Basic':
            return None
        return auth[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """decodes a base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None
