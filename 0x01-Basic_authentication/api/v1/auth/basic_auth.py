#!/usr/bin/env python3
"""
BasicAuth class
"""


from api.v1.auth.auth import Auth
# from typing import TypeVar
# from models.user import User
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
