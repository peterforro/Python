import os
import turtle 
import math


def set_start_post(x):
    turtle.up()
    turtle.setpos(x,0)
    turtle.down()


def x_coordinate(v0,t,alfa):
    return v0 * t * math.cos(math.radians(alfa))


def y_coordinate(v0,t,alfa):
    return v0 * t * math.sin(math.radians(alfa)) - 0.5 * 9.81 * t**2


def square(a_side,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a_side)
        turtle.left(90)
    turtle.end_fill()


def go_forward(distance):
    turtle.forward(distance)


def go_backward(distance):
    turtle.backward(distance)


def init_battlefield(distance,a_side):
    go_forward(distance)
    square(a_side,'black')
    go_backward(distance)


def hit_check(x,y,distance,a_side):
    return x>=distance and x<=distance+a_side and y>=0 and y<=a_side 


def trajectory(distance,a_side,alfa,v0,delta_t):
    turtle.pencolor('red')
    t,y = 0,1
    while(y >= 0):
        x = x_coordinate(v0,t,alfa)
        y = y_coordinate(v0,t,alfa)
        turtle.setpos(x,y)
        print(f't={round(t,2)} x={round(x,2)} y={round(y,2)}')
        t += delta_t
        if hit_check(x,y,distance,a_side):
            print('Target has been destroyed!')
            return
    print('Target missed!')


def input_parameters():
    distance = float(input("distance?: "))
    a_side = float(input('a_side?: '))
    alfa = float(input('alfa?: '))
    v0 = float(input('v0?: '))
    delta_t = float(input('delta_t?: '))
    return distance, a_side, alfa, v0, delta_t


def main():
    os.system('clear')
    distance, a_side, alfa, v0, delta_t = input_parameters()
    init_battlefield(distance,a_side)
    trajectory(distance,a_side,alfa,v0,delta_t)
    turtle.mainloop()
    



if __name__ == '__main__':
    main()
