from window import *
from maze import Maze

def main():
    win = Window(800, 600)

    num_cols = 14
    num_rows = 10
    m1 = Maze(50, 50, num_rows, num_cols, 50, 50, win)

    win.wait_for_close()

main()