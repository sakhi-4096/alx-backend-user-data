#!/usr/bin/env python3
"""Database module for user management.
"""

from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """Database interface for user management."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        # Create an SQLite engine
        self._engine = create_engine("sqlite:///a.db", echo=False)
        # Create tables if they don't exist
        Base.metadata.create_all(self._engine)
        # Initialize session
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): Email address of the user.
            hashed_password (str): Hashed password of the user.
        Returns:
            User: The newly created user object or None if failed.
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
            return new_user
        except Exception:
            self._session.rollback()
            return None

    def find_user_by(self, **kwargs) -> User:
        """Find a user based on a set of filters.

        Args:
            **kwargs: Arbitrary keyword arguments to filter users.
        Returns:
            User: The found user object.
        Raises:
            InvalidRequestError: If an invalid filter is provided.
            NoResultFound: If no user is found.
        """
        fields, values = [], []
        for key, value in kwargs.items():
            if hasattr(User, key):
                fields.append(getattr(User, key))
                values.append(value)
            else:
                raise InvalidRequestError(f"Invalid filter: {key}")
        result = self._session.query(User).filter(
            tuple_(*fields).in_([tuple(values)])
        ).first()
        if result is None:
            raise NoResultFound("No user found with given filters.")
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user based on a given id.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments to update user fields.
        Raises:
            ValueError: If an invalid field is provided.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_source = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_source[getattr(User, key)] = value
            else:
                raise ValueError(f"Invalid field: {key}")
        self._session.query(User).filter(User.id == user_id).update(
            update_source,
            synchronize_session=False,
        )
        self._session.commit()
