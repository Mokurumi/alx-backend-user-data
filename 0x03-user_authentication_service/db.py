#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user to the database
        """
        try:
            new_user = User(email, hashed_password)
            self._session.add(new_user)
            self._session.commit()
            # Ensure the user object is refreshed from the database
            self._session.refresh(new_user)
        except Exception as e:
            self._session.rollback()
            new_user = None
        finally:
            self._session.close()
            self.__session = None  # Ensure the session is reset
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.
        """
        session = self._session
        query = session.query(User)
        try:
            user = query.filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound()
            return user
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.
        """
        session = self._session  # get the session
        user = self.find_user_by(id=user_id)  # find the user by id
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"User has no attribute '{key}'")
            setattr(user, key, value)
        session.commit()
