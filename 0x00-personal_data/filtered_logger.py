#!/usr/bin/env python3
"""
Filtering module
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    return re.sub(r'(\b(?:' + '|'.join(fields) + r')\b)=\S+',
                  lambda x: x.group(1) + '=' + redaction,
                  message)
