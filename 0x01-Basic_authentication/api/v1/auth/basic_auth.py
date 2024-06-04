#!/usr/bin/env python3
"""
BasicAuth class
Add the method def decode_base64_authorization_header(self, base64_authorization_header: str) -> str: in the class BasicAuth that returns the decoded value of a Base64 string base64_authorization_header:

Return None if base64_authorization_header is None
Return None if base64_authorization_header is not a string
Return None if base64_authorization_header is not a valid Base64 - you can use try/except
Otherwise, return the decoded value as UTF8 string - you can use decode('utf-8')

Add the method def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str) in the class BasicAuth that returns the user email and password from the Base64 decoded value.

This method must return 2 values
Return None, None if decoded_base64_authorization_header is None
Return None, None if decoded_base64_authorization_header is not a string
Return None, None if decoded_base64_authorization_header doesn’t contain :
Otherwise, return the user email and the user password - these 2 values must be separated by a :
You can assume decoded_base64_authorization_header will contain only one :
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
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ extract_user_credentials method
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(':', 1)
        return user_credentials[0], user_credentials[1]
