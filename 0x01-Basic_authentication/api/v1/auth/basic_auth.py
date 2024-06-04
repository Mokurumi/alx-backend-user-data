#!/usr/bin/env python3
"""
BasicAuth class

Add the method def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'): in the class BasicAuth that returns the User instance based on his email and password.

Return None if user_email is None or not a string
Return None if user_pwd is None or not a string
Return None if your database (file) doesn’t contain any User instance with email equal to user_email - you should use the class method search of the User to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.
Return None if user_pwd is not the password of the User instance found - you must use the method is_valid_password of User
Otherwise, return the User instance
"""


from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header method
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
          """ decode_base64_authorization_header method
          """
            # if base64_authorization_header is None:
            #     return None
            # if type(base64_authorization_header) is not str:
            #     return None
            try:
                str_bytes = base64.b64decode(
                    base64_authorization_header,
                    validate=True
                )
                return str_bytes.decode('utf-8')
        except Exception:
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ extract_user_credentials method
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        user_credentials = decoded_base64_authorization_header.split(':', 1)
        if len(user_credentials) != 2:
            return (None, None)
        return (user_credentials[0], user_credentials[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        """ user_object_from_credentials method
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
