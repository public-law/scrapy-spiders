"""
This type stub file was generated by pyright.
"""

from twisted.internet.base import ThreadedResolver
from scrapy.utils.datatypes import LocalCache
from typing import Any, Optional

dnscache = LocalCache(10000)
class CachingThreadedResolver(ThreadedResolver):
    def __init__(self, reactor, cache_size, timeout):
        self.timeout = ...
    
    def getHostByName(self, name, timeout: Optional[Any] = ...):
        ...
    
    def _cache_result(self, result, name):
        ...
    


