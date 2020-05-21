"""
This type stub file was generated by pyright.
"""

import marshal
from six.moves import cPickle as pickle
from queuelib import queue

"""
Scheduler queues
"""
def _serializable_queue(queue_class, serialize, deserialize):
    class SerializableQueue(queue_class):
        ...
    
    

def _pickle_serialize(obj):
    ...

PickleFifoDiskQueue = _serializable_queue(queue.FifoDiskQueue, _pickle_serialize, pickle.loads)
PickleLifoDiskQueue = _serializable_queue(queue.LifoDiskQueue, _pickle_serialize, pickle.loads)
MarshalFifoDiskQueue = _serializable_queue(queue.FifoDiskQueue, marshal.dumps, marshal.loads)
MarshalLifoDiskQueue = _serializable_queue(queue.LifoDiskQueue, marshal.dumps, marshal.loads)
FifoMemoryQueue = queue.FifoMemoryQueue
LifoMemoryQueue = queue.LifoMemoryQueue