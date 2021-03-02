# implementation classes

from iobject import IObject

class A(IObject):
    def execute(self):
        print("Executing implementation of Class A")

class B(IObject):
    def execute(self):
        print("Executing implementation of Class B")
