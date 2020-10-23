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
    turtle.done()

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


