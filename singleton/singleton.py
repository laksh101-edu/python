# singleton.py

class Singleton:

    __instance = None

    @staticmethod
    def get_instance():
        pass

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Class is singleton")
        else:
            Singleton.__instance = self
