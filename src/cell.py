from graphics import *

class Cell:
    def __init__(self, win):
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
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

        if self.has_left_wall:
            left_wall_line = Line(top_left, bottom_left)
            self._win.draw_line(left_wall_line, 'blue')
            
        if self.has_right_wall:
            right_wall_line = Line(top_right, bottom_right)
            self._win.draw_line(right_wall_line, 'blue')

        if self.has_top_wall:
            top_wall_line = Line(top_left, top_right)
            self._win.draw_line(top_wall_line, 'blue')

        if self.has_bottom_wall:
            bottom_wall_line = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall_line, 'blue')