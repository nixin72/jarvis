class User:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @staticmethod
    def getUser():
        return User("Philip")