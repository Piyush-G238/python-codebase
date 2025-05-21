
class Test:
    def __init__(self):
        self.__name = "Piyush"
        pass

    def get_name(self):
        return self.__name

    def public(self):
        print("public")

    def _private(self):
        print("private")

obj = Test()
print(obj.get_name())
obj.public()
obj._private()
