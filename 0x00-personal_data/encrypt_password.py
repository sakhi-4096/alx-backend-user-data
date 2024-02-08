#!/usr/bin/env python3
"""A module for encrypting and validating passwords using bcrypt."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with a random salt.

    Args:
        password (str): The password to be hashed.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(stored_pwd: bytes, input_pwd: str) -> bool:
    """Checks if a password matches its hashed version.

    Args:
        hashed_password (bytes): The hashed password to be validated.
        password (str): The password to be checked.
    Returns:
        bool: True if the password matches its hashed version, False otherwise.
    """
    return bcrypt.checkpw(input_pwd.encode(), stored_pwd)
