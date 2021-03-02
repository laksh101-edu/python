# factory.py

from registry import registry

class FactoryClazz:

    def get_class(self, key):
        if key in registry:
            return self.load_class(registry.get(key))
        else:
            raise ValueError("Key {} not found in registry".format(registry))


    def load_class(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )

        for comp in parts[1:]:
            m = getattr(m, comp)

        return m
