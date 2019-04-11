class Util:

    def __init__(self):
        self.__numbers = []


    def add(self,*values):
        for value in values:
            self.__numbers.append(value)
            print('added!')


    def __str__(self):
        return ', '.join([str(value) for value in self.__numbers])