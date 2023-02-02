#!/usr/bin/env python3
"""encrypting passwors"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> bytes:
    "function to hash a password salted with byte string"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
