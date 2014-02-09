__author__ = 'JacobBillings'

from graphics import *
win = GraphWin("J.A.I",640,480)
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

    text = Text(Point(0.25,3.75),"J.A.I")
    text.setFace('helvetica')
    text.setStyle("bold")
    text.setSize(36)
    text.setTextColor("white")
    text.draw(win)
    #line = Line(Point(0,3),Point(3,3))
    #line.draw(win)


    input('Press enter to close')
    win.quit()



if __name__ == '__main__':
    main()