#!/usr/bin/env python3
"""
SessionDBAuth class
"""


from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """
    def create_session(self, user_id: str = None) -> str:
        """ create_session method
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id_for_session_id method
        """
        if session_id is None or type(session_id) is not str:
            return None
        user_session = UserSession.search({"session_id": session_id})
        if not user_session:
            return None
        if self.session_duration <= 0:
            return user_session[0].user_id
        if user_session[0].created_at + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None
        return user_session[0].user_id

    def destroy_session(self, request=None):
        """ destroy_session method
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if not user_session:
            return False
        user_session[0].remove()
        return True
