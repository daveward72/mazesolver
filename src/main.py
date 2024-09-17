from window import *
from cell import *

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(100, 100, 200, 200)

    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.has_top_wall = False
    cell2.draw(300, 300, 400, 400)

    cell1.draw_move(cell2, True)

    win.wait_for_close()

main()