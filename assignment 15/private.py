class Cup:
    def __init__(self,color):
        self.color = color
        self.__content = None #private variable

    def fill(self,beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None