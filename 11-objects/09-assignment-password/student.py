class Password:
    def __init__(self, pwd):
        self.__password = pwd

    def verify(self, string):
        return string == self.__password
