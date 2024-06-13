#!/usr/bin/env python3
"""
Auth module
"""


import bcrypt
from db import DB
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID
    """
    return str(uuid4())


class Auth:
    '''Auth class to interact with the authentication database.
    '''

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except ValueError:
            pass
        return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except ValueError:
            return False
        except Exception:
            return False
