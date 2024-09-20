import time

from cell import *

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            col_of_cells = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                col_of_cells.append(cell)
            self._cells.append(col_of_cells)

        for i in range(len(self._cells)):
            col_of_cells = self._cells[i]
            for j in range(len(col_of_cells)):
                cell = col_of_cells[j]
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        left_x = self._x1 + i * self._cell_size_x
        top_y = self._y1 + j * self._cell_size_y
        right_x = left_x + self._cell_size_x
        bottom_y = top_y + self._cell_size_y

        if self._win is None:
            return
        
        cell.draw(left_x, top_y, right_x, bottom_y)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_right_cell = self._cells[self._num_cols-1][self._num_rows-1]
        bottom_right_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

