# Case-study #1
# Developers: Marinkin O. (),
# Seledtsov A. (),
# Evdischenko M. ()


import turtle
import math


def circle(x, y, radius, angle, color):
    '''
    Function, drawing circle
    :param x: coordinate X of point on the side of the circle
    :param y: coordinate Y of point on the side of the circle
    :param radius: radius of a circle
    :param angle: orientation change
    :param color: color of a circle frame and fill
    :return: None
    ToDo: Evdischenko
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.left(angle)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()

    
def oval(x, y, radius, angle, color):
    '''
    Function, drawing oval
    :param x: coordinate X of point on the side of the oval
    :param y: coordinate Y of point on the side of the oval
    :param radius: radius of the oval part
    :param angle: orientation change
    :param color: color of a oval frame and fill
    :return: None
    ToDo: Evdischenko
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.left(angle)
    turtle.circle(radius, 90)
    turtle.circle(radius / 2, 90)
    turtle.circle(radius, 90)
    turtle.circle(radius / 2, 90)
    turtle.end_fill()
    turtle.up()

    
def octagon(x, y, side, angle, color):
    '''
    Function, drawing octagon
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a octagon
    :param angle: orientation change
    :param color: color of a octagon frame and fill
    :return: None
    ToDo: Evdischenko
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)
    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.forward(side)
    turtle.right(360 / 8)
    turtle.end_fill()
    turtle.up()
    
    
def trapeze(x, y, side, angle, color):
    '''
    Function, drawing trapeze
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a trapeze
    :param angle: the mounting angle of a trapeze
    :param color: color of a trapeze frame and fill
    :return: None
    ToDo: Marinkin
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)
    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.left(60)
    turtle.forward(side)
    turtle.left(60)
    turtle.forward(side)
    turtle.end_fill()
    turtle.up()

    
def triangle60(x, y, side, angle, color):
    '''
    Function, drawing equilateral triangle
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a triangle
    :param angle: the mounting angle of a triangle
    :param color: color of a triangle frame and fill
    :return: None
    ToDo: Marinkin
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    turtle.up()
    

def square(x, y, side, angle, color):
    '''
    Function, drawing square
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a square
    :param angle: the mounting angle of a square
    :param color: color of a square frame and fill
    :return: None
    ToDo: Seledtsov
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

    
def rectangle(x, y, width, length, angle, color):
    '''
    Function, drawing rectangle
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param width: side width of a rectangle
    :param length: side length of a rectangle
    :param angle: the mounting angle of a rectangle
    :param color: color of a rectangle frame and fill
    :return: None
    ToDo: Seledtsov
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

    
def parallelogram(x, y, width, length, angle, color):
    '''
    Function, drawing parallelogram
    :param x: upper left corner
    coordinate X
    :param y: upper left corner coordinate Y
    :param width: side width of a parallelogram
    :param length: side length of a parallelogram
    :param angle: the mounting angle of a parallelogram
    :param color: color of a parallelogram frame and fill
    :return: None
    ToDo: Seledtsov
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(width)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(120)
    turtle.end_fill()
    turtle.up()

    
def triangle90(x, y, side, angle, color):
    '''
    Function, drawing triangle with an angle of 90 degrees
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: length of side of a triangle
    :param angle: the mounting angle of a triangle
    :param color: color of a triangle frame and fill
    :return: None
    ToDo: Seledtsov
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(135)
    turtle.forward(math.sqrt((side ** 2) + (side ** 2)))
    turtle.end_fill()
    turtle.up()


def rocket():
    '''
    Function, drawing rocket
    :return: None
    ToDo: Seledtsov
    '''
    turtle.shape('turtle')
    turtle.speed(10)
    triangle60(-830, -430, 140, 270, 'tomato')
    rectangle(-828, -130, 200, 300, 0, 'darkgrey')
    triangle60(-626, -290, 140, 90, 'tomato')
    triangle60(-828, -128, 200, 0, 'tomato')
    circle(-750, -200, 30, 300, 'white')
    circle(-750, -300, 30, 300, 'white')
    circle(-750, -400, 30, 300, 'white')
    trapeze(-655, -492, 70, 240, 'orange')
    turtle.home()
    pass


def rabbit():
    '''
    Function, drawing rabbit
    :return: None
    ToDo: Seledtsov
    '''
    turtle.shape('turtle')
    turtle.speed(10)
    triangle90(-828, 120, 100, 0, 'dodgerblue')
    triangle90(-726, 195, 75, 90, 'purple')
    triangle90(-691, 260, 140, 180, 'yellow')
    triangle90(-831, 262, 140, 0, 'red')
    triangle60(-688, 297, 70, 90, 'magenta')
    square(-688, 437, 70, 0, 'orange')
    parallelogram(-653, 439, 70, 70, 240, 'lime')
    turtle.home()
    pass
  
  
  def robot():
    '''
    Function, drawing robot
    :return: None
    ToDo: Marinkin
    '''
    turtle.speed(10)
    triangle60(-40, -500, 20, 0, 'blue')
    triangle60(40,  -500, 20, 0, 'blue')
    rectangle(-38, -415, 15, 70, 0, 'red')
    turtle.up()
    rectangle(42, -415, 15, 70, 0, 'red')
    turtle.up()
    square(-65, -270,150,0,"blue")
    turtle.up()
    rectangle(-137, -260, 290, 10, 0, 'red')
    turtle.up()
    circle(-100, -310, 20, 0, 'blue')
    rectangle(-110, -310, 20, 50, 0, 'red')
    circle(-100, -400, 20, 0, 'blue')
    circle(120, -310, 20, 0, 'blue')
    rectangle(110, -310, 20, 50, 0, 'red')
    circle(120, -400, 20, 0, 'blue')
    square(-15, -210, 50, 0, 'blue')
    trapeze(49,-210, 40, 240, 'red' )
    circle(-2, -230, 3, 0, "black")
    circle(25, -230, 3, 0, "black")
    square(10, -280, 8, 45, 'black')
    square(10, -300, 8, 45, 'black')
    square(10, -320, 8, 45, 'black')
    square(10, -340, 8, 45, 'black')



def bull():
    '''
    Function, drawing bull
    :return: None
    ToDo: Marinkin
    '''
    turtle.speed(10)
    triangle90(0, 100, 100, -45, "black")
    triangle90(129, 112, 80, -135, 'red')
    triangle90(146, 100, 100, -90, 'black' )
    parallelogram(147, 190, 65, 15, 50, 'yellow')
    square(-62, 260, 60, 0, 'red')
    oval(-65, 280, 20, 90, 'grey')
    oval(5, 275, 20, -25, 'orange')
    turtle.up()
