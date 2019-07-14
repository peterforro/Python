from threading import Thread
from time import sleep


class test1(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__counter = 0

    def run(self):
        while(True):
            self.__counter += 1
            print(self.__counter)
            sleep(0.3)


class test2(Thread):
    def __init__(self):
        Thread.__init__(self)


    def run(self):
        while(True):
            print("hello")
            sleep(1)





if __name__ == "__main__":
    test1 = test1()
    test2 = test2()    
    test2.start()
    test1.start()