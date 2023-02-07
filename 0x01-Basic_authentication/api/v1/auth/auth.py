#!/usr/bin/env python3
"""auth module"""
from typing import List
from typing import TypeVar
from flask import request


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """require auth"""
        if not path:
            return True
        if not excluded_path:
            return True
        path_with_slash = path
        if path[-1] == '/':
            path_with_slash = path_with_slash.rstrip(path_with_slash[-1])
        else:
            path_with_slash += '/'
        for i in excluded_path:
            if path_with_slash in i or path in i:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """get current user"""
        return None
