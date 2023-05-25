#!/usr/bin/env python3
'''Encrypting passwords'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''
    hash password
    '''
    byte_password = password.encode()
    hashed_pass = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    return hashed_pass


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Check if password is valid
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
