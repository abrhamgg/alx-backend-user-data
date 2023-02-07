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
        if path_with_slash in excluded_path or path in excluded_path:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get current user"""
        return None
