# client.py


from factory import FactoryClazz

class Client:

    def do_something(self):
        inst = FactoryClazz()
        iobject_ref = inst.get_class(key="key_b")
        iobject_ref().execute()


if __name__ == '__main__':
    Client().do_something()
