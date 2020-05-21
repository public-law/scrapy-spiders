"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
This module provides some commonly used processors for Item Loaders.

See documentation in docs/topics/loaders.rst
"""
class MapCompose(object):
    def __init__(self, *functions, **default_loader_context):
        self.functions = ...
        self.default_loader_context = ...
    
    def __call__(self, value, loader_context: Optional[Any] = ...):
        ...
    


class Compose(object):
    def __init__(self, *functions, **default_loader_context):
        self.functions = ...
        self.stop_on_none = ...
        self.default_loader_context = ...
    
    def __call__(self, value, loader_context: Optional[Any] = ...):
        ...
    


class TakeFirst(object):
    def __call__(self, values):
        ...
    


class Identity(object):
    def __call__(self, values):
        ...
    


class SelectJmes(object):
    """
        Query the input string for the jmespath (given at instantiation),
        and return the answer
        Requires : jmespath(https://github.com/jmespath/jmespath)
        Note: SelectJmes accepts only one input element at a time.
    """
    def __init__(self, json_path):
        self.json_path = ...
        self.compiled_path = ...
    
    def __call__(self, value):
        """Query value for the jmespath query and return answer
        :param value: a data structure (dict, list) to extract from
        :return: Element extracted according to jmespath query
        """
        ...
    


class Join(object):
    def __init__(self, separator=...):
        self.separator = ...
    
    def __call__(self, values):
        ...
    

