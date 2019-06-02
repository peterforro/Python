from random import randint
from os import system


class FloodFill: 


    def __init__(self):
        '''
        Constructor method
        Asks for user input to initialize the paramaters of the maze (matrix) - width, height, number of walls,
        and starting coordinates of the filling.
        '''
        self.__wall = '\033[93m' + '\u258A' + '\033[0m'
        self.__visited = '\033[92m' + '\u258A' + '\033[0m'
        self.__not_visited = '\33[30m' + '\u258A' + '\033[0m'
        self.__width = int(input('width?: '))
        self.__height = int(input('height?: '))
        self.__wall_num = int(input('number of walls?: '))
        self.__Matrix = [[self.__not_visited for x in range(self.__width)] for y in range(self.__height)]
        self.__generate_walls()
        self.wall_coordinates = []

                                   
    def __generate_walls(self):
        '''
        Randomly generates walls in the matrix. The number of the walls is given as a user input (__init__() method)
        '''
        wall_cnt = 0
        while(wall_cnt != self.__wall_num):
            cors =  (randint(0, self.__height - 1), randint(0, self.__width - 1))
            if self.__Matrix[cors[0]][cors[1]] != self.__wall:
                self.__Matrix[cors[0]][cors[1]] = self.__wall
                wall_cnt += 1


    def fill(self, xCor, yCor):
        '''
        Recursive solution of the FloodFill algorithm, implemented by myself
        '''
        if xCor < 0 or xCor >= self.__width or yCor < 0 or yCor >= self.__height:
            return
        if self.__Matrix[yCor][xCor] == self.__wall:
                self.wall_coordinates.append((yCor,xCor))
        if self.__Matrix[yCor][xCor] != self.__not_visited:
            return
        self.__Matrix[yCor][xCor] = self.__visited
        print(self)
        for nextStep in [(xCor, yCor - 1), (xCor, yCor + 1), (xCor - 1, yCor), (xCor + 1, yCor)]:
            self.fill(*nextStep)


    def __str__(self):
        '''
        Clears the terminal and returns with the string representation of the matrix
        '''
        system('cls')
        strRepr = ''
        for y in range(self.__height):
            for x in range(self.__width):
                strRepr += self.__Matrix[y][x]
            strRepr += '\n'
        return strRepr

        

if __name__ == '__main__':
    floodFill = FloodFill()
    print(floodFill)
    xCor = int(input('xCor?: '))
    yCor = int(input('yCor?: '))
    floodFill.fill(xCor, yCor)
    input()
    print("\n".join([f'{i+1}: {cors}' for i,cors in enumerate(set(floodFill.wall_coordinates))]))