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
