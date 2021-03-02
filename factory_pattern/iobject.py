# iobject.py

import abc

class IObject:

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError("IObject does not provide implementation for execute method")
