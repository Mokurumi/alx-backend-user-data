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
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session  # get the session
        try:
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments.
        """
        session = self._session
        query = session.query(User)
        try:
            user = query.filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        return user