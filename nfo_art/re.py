"""
re utils
"""
from . import EOF_BYTE

import re


eof_pattern = re.compile(EOF_BYTE)
