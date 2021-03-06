"""
This type stub file was generated by pyright.
"""

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)
class MiddlewareManager(object):
    """Base class for implementing middleware managers"""
    component_name = ...
    def __init__(self, *middlewares):
        self.middlewares = ...
        self.methods = ...
    
    @classmethod
    def _get_mwlist_from_settings(cls, settings):
        ...
    
    @classmethod
    def from_settings(cls, settings, crawler: Optional[Any] = ...):
        ...
    
    @classmethod
    def from_crawler(cls, crawler):
        ...
    
    def _add_middleware(self, mw):
        ...
    
    def _process_parallel(self, methodname, obj, *args):
        ...
    
    def _process_chain(self, methodname, obj, *args):
        ...
    
    def _process_chain_both(self, cb_methodname, eb_methodname, obj, *args):
        ...
    
    def open_spider(self, spider):
        ...
    
    def close_spider(self, spider):
        ...
    


