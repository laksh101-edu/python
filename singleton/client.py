# singleton client

from singleton import Singleton

if __name__ == '__main__':
    inst = Singleton()
    print(inst)

    inst = Singleton.get_instance()
    print(inst)
