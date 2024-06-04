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
          if base64_authorization_header is None:
                return None
          if not isinstance(base64_authorization_header, str):
                return None
          try:
                const decoded = base64.b64decode(
                    base64_authorization_header,
                    validate=True
                )
                return decoded.decode('utf-8')
          except (binascii.Error, UnicodeDecodeError):
                return None
