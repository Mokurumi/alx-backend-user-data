#!/usr/bin/env python3
"""
BasicAuth class
Add the method def decode_base64_authorization_header(self, base64_authorization_header: str) -> str: in the class BasicAuth that returns the decoded value of a Base64 string base64_authorization_header:

Return None if base64_authorization_header is None
Return None if base64_authorization_header is not a string
Return None if base64_authorization_header is not a valid Base64 - you can use try/except
Otherwise, return the decoded value as UTF8 string - you can use decode('utf-8')
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
            if base64_authorization_header is None:
                return None
            if type(base64_authorization_header) is not str:
                return None
            try:
                base64_bytes = base64_authorization_header.encode('utf-8')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('utf-8')
                return message
            except binascii.Error:
                return None
