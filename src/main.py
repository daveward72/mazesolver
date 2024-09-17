from window import *
from graphics import *

def main():
    win = Window(800, 600)

    p1 = Point(200, 500)
    p2 = Point(600, 100)
    l1 = Line(p1, p2)
    win.draw_line(l1, 'green')

    p3 = Point(400, 100)
    p4 = Point(500, 500)
    l2 = Line(p3, p4)
    win.draw_line(l2, 'red')

    win.wait_for_close()

main()