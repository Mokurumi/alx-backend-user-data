#!/usr/bin/env python3
'''
encrypt_password.py
'''


import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Returns a salted, hashed password, which is a byte string.
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Returns a boolean.
    '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
