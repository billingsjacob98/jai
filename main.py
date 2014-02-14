__author__ = 'JacobBillings'

from graphics import *
win = GraphWin("J.A.I",1400,680)
win.setCoords(0.0,0.0,3.0,4.0)



def main():
    rect = Rectangle(Point(0,3.5),Point(3.5,4.5))
    rect.draw(win)
    rect.setFill("blue")
    rect.setOutline("white")
    rect.setFill(color_rgb(46,100,254))
    rect.setWidth(2)

    rect = Rectangle(Point(0,0),Point(0.5,3.5))
    rect.draw(win)
    rect.setFill(color_rgb(46,100,254))
    rect.setOutline("white")
    rect.setWidth(2)

    line = Line(Point(0.5,3.5),Point(1,4.5))
    line.setFill("white")
    line.draw(win)
    line.setWidth(2)

    line = Line(Point(0.75,3.515),Point(0.75,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(1,3.515),Point(1,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(1.25,3.515),Point(1.25,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(1.5,3.515),Point(1.5,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(1.75,3.515),Point(1.75,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(2,3.515),Point(2,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(2.25,3.515),Point(2.25,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(2.5,3.515),Point(2.5,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(2.75,3.515),Point(2.75,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(3,3.515),Point(3,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(3.15,3.515),Point(3.15,4.5))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(0.51,3.515),Point(3.15,3.515))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(0.567,3.630),Point(3.15,3.630))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(0.63,3.745),Point(3.15,3.745))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(0.685,3.860),Point(3.15,3.860))
    line.setFill("black")
    line.draw(win)

    line = Line(Point(0.75,3.975),Point(3.15,3.975))
    line.setFill("black")
    line.draw(win)

    text = Text(Point(0.25,3.75),"J.A.I")
    text.setFace('helvetica')
    text.setStyle("bold")
    text.setSize(36)
    text.setTextColor("white")
    text.draw(win)

    text = Text(Point(1.75,3.75),"Command Line Terminal")
    text.setFace('helvetica')
    text.setStyle("bold")
    text.setSize(36)
    text.setTextColor("white")
    text.draw(win)

    text = Text(Point(0.7,3.35), 'Hello Mr Billings')
    text.setFace('courier')
    text.setSize(14)
    text.draw(win)
    promptinput = Entry(Point(0.7,3.45), 100)
    # promptinput.setFill('white')
    #promptinput.setOutline('white')
    promptinput.draw(win)


    #line = Line(Point(0,3),Point(3,3))
    #line.draw(win)

    #when drawing objects point correspond to a math graph

    input('Press enter to close')
    win.quit()


main()