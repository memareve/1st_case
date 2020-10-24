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
    turtle.goto(-765, 70)
    turtle.pencolor('black')
    turtle.write('This is a rocket')
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
    turtle.goto(-890, 395)
    turtle.pencolor('black')
    turtle.write('This is a rabbit')
    turtle.home()
    pass


#drawing images:
rocket()
rabbit()
turtle.done()
