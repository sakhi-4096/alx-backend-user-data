#!/usr/bin/env python3
"""Module for authentication-related routines."""
import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password.

    Args:
        password (str): The password to hash.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a UUID.

    Returns:
        str: The generated UUID as a string.
    """
    return str(uuid4())


class Auth:
    """Class to handle authentication-related operations."""

    def __init__(self):
        """Initializes a new Auth instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
        Returns:
            User: The newly registered user.
        Raises:
            ValueError: If the user already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user login credentials.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> Union[str, None]:
        """Creates a new session for the user.

        Args:
            email (str): The email of the user.
        Returns:
            Union[str, None]: The session ID if created, None otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            pass
        return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieves a user based on the session ID.

        Args:
            session_id (str): The session ID.
        Returns:
            Union[User, None]: The user object if found, None otherwise.
        """
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session associated with the user.

        Args:
            user_id (int): The ID of the user.
        """
        if user_id is not None:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token for the user.

        Args:
            email (str): The email of the user.
        Returns:
            str: The generated reset token.
        Raises:
            ValueError: If the user does not exist.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
        except NoResultFound:
            pass
        raise ValueError("User does not exist")

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates the user's password using the reset token.

        Args:
            reset_token (str): The reset token.
            password (str): The new password.
        Raises:
            ValueError: If the reset token is invalid.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user is not None:
                new_password_hash = _hash_password(password)
                self._db.update_user(
                    user.id,
                    hashed_password=new_password_hash,
                    reset_token=None,
                )
                return
        except NoResultFound:
            pass
        raise ValueError("Invalid reset token")
