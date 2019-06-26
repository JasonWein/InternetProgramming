## Jason Wein
## Jan 30, 2019
## Internet Programming
#Homework 2
#Python graphing program that displays the function y=x^2.
from graphics import *
def main():
    # Create a 200x200 window.
    win = GraphWin("My Graph", 200, 200)
    Line(Point(100,0),Point(100,199)).draw(win)
    Line(Point(0,100),Point(199,100)).draw(win)
    #for all i from 0 to 200, create points in the form of y=x^2.
    for i in range(0,200):
        x = (i-100)/100
        y=x*x
        yy=100-y*100
        aPoint = Point(i,yy)
        aPoint.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
