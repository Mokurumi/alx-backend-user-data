#!/usr/bin/env python3
'''
This module contains the function filter_datum

Use user_data.csv for this task

Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.

Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.


'''


import re
from typing import List
import logging
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(ch)
    return logger
