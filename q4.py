'''
Created on 12/09/2014

@author: lee
'''

import turtle

def main():
    path_data = open('path.txt').read()
    
    print turtle.position()
    turtle.penup()
    turtle.setposition(-400,200)
    turtle.pendown()
    turtle.speed(0)
    turtle.delay(0)
    for c in path_data:
        if c in 'NSEW*':
            if c == 'N':
                turtle.setheading(90)
                turtle.forward(1)
            if c == 'S':
                turtle.setheading(270)
                turtle.forward(1)
            if c == 'E':
                turtle.setheading(0)
                turtle.forward(1)
            if c == 'W':
                turtle.setheading(180)
                turtle.forward(1)
            if c == '*':
                if turtle.isdown():
                    turtle.penup()
                else:
                    turtle.pendown()


if __name__ == '__main__':
    main()