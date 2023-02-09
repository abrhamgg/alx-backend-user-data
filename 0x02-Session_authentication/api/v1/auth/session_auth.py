#!/usr/bin/env python3
"""Empty session"""
from api.v1.auth.auth import Auth
from uuid import uuid4

from api.v1.views import users


class SessionAuth(Auth):
    """Session Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session method"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id by session"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """current user"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return users.get(user_id)
