"""
This type stub file was generated by pyright.
"""

from threading import RLock
from typing import Any, Optional

_fill_lock = RLock()
class LazyDict(DictMixin):
    """Dictionary populated on first use."""
    data = ...
    def __getitem__(self, key):
        ...
    
    def __contains__(self, key):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def keys(self):
        ...
    


class LazyList(list):
    """List populated on first use."""
    _props = ...
    def __new__(cls, fill_iter: Optional[Any] = ...):
        class LazyList(list):
            ...
        
        
    


class LazySet(set):
    """Set populated on first use."""
    _props = ...
    def __new__(cls, fill_iter: Optional[Any] = ...):
        class LazySet(set):
            ...
        
        
    

