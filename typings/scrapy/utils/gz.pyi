"""
This type stub file was generated by pyright.
"""

import six
import re
from scrapy.utils.decorators import deprecated

if six.PY2:
    def read1(gzf, size=...):
        ...
    
else:
    def read1(gzf, size=...):
        ...
    
def gunzip(data):
    """Gunzip the given data and return as much data as possible.

    This is resilient to CRC checksum errors.
    """
    ...

_is_gzipped = re.compile(rb'^application/(x-)?gzip\b', re.I).search
_is_octetstream = re.compile(rb'^(application|binary)/octet-stream\b', re.I).search
@deprecated
def is_gzipped(response):
    """Return True if the response is gzipped, or False otherwise"""
    ...

def gzip_magic_number(response):
    ...

