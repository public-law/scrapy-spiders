"""
This type stub file was generated by pyright.
"""

def listen_tcp(portrange, host, factory):
    """Like reactor.listenTCP but tries different ports in a range."""
    ...

class CallLaterOnce(object):
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """
    def __init__(self, func, *a, **kw):
        ...
    
    def schedule(self, delay=...):
        ...
    
    def cancel(self):
        ...
    
    def __call__(self):
        ...
    

