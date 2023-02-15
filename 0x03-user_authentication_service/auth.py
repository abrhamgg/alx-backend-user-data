#!/usr/bin/env python3
"""auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hash a password and returns a byte"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
