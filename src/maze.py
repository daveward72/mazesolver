import time
import random

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
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed != None:
            random.seed(seed)    

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while True:
            to_visit = []
            for dir in dirs:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if new_i >= 0 and new_i < self._num_cols and new_j >= 0 and new_j < self._num_rows and not self._cells[new_i][new_j].visited:
                    to_visit.append((new_i, new_j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
                
            random_dir = random.choice(to_visit)
            self._break_walls(i, j, random_dir[0], random_dir[1])
            self._break_walls_r(random_dir[0], random_dir[1])

    def _break_walls(self, i1, j1, i2, j2):
        if i1 < i2:
            self._cells[i1][j1].has_right_wall = False
            self._cells[i2][j2].has_left_wall = False
        elif i1 > i2:
            self._cells[i1][j1].has_left_wall = False
            self._cells[i2][j2].has_right_wall = False
        elif j1 < j2:
            self._cells[i1][j1].has_bottom_wall = False
            self._cells[i2][j2].has_top_wall = False
        elif j2 < j1:
            self._cells[i1][j1].has_top_wall = False
            self._cells[i2][j2].has_bottom_wall = False

        self._draw_cell(i1, j1)
        self._draw_cell(i2, j2)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False