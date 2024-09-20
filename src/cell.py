from graphics import *

class Cell:
    def __init__(self, win = None):
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if x2 <= x1:
            raise ValueError("x2 must be greater than x1")
        
        if y2 <= y1:
            raise ValueError("y2 must be greater than y1")

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_right = Point(x2, y2)
        bottom_left = Point(x1, y2)


        left_wall_line = Line(top_left, bottom_left)
        color = 'blue' if self.has_left_wall else '#d9d9d9'
        self._win.draw_line(left_wall_line, color)

        right_wall_line = Line(top_right, bottom_right)
        color = 'blue' if self.has_right_wall else '#d9d9d9'
        self._win.draw_line(right_wall_line, color)

        top_wall_line = Line(top_left, top_right)
        color = 'blue' if self.has_top_wall else '#d9d9d9'
        self._win.draw_line(top_wall_line, color)

        bottom_wall_line = Line(bottom_left, bottom_right)
        color = 'blue' if self.has_bottom_wall else '#d9d9d9'
        self._win.draw_line(bottom_wall_line, color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        center_self_x = (self._x1 + self._x2) // 2
        center_self_y = (self._y1 + self._y2) // 2
        center_self_point = Point(center_self_x, center_self_y)

        center_to_x = (to_cell._x1 + to_cell._x2) // 2
        center_to_y = (to_cell._y1 + to_cell._y2) // 2
        center_to_point = Point(center_to_x, center_to_y)

        color = "red" if undo else "gray"
        line = Line(center_self_point, center_to_point)
        self._win.draw_line(line, color)