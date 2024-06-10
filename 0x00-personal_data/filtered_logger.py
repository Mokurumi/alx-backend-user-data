#!/usr/bin/env python3
'''
This module contains the function filter_datum
'''


import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Constructor
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format method
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
