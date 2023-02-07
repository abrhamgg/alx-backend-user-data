#!/usr/bin/env python3
"""auth module"""
from typing import List
from typing import TypeVar
from flask import request


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get current user"""
        return None
