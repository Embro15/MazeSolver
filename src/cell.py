from tkinter import Canvas
from point import Point, Line
from window import Window

class Cell:
    def __init__(
            self, 
            win=None,
            has_left_wall=True,  
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True
            ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_right_wall
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(
            self, 
            x1, 
            y1, 
            x2, 
            y2, 
            has_left_wall=True,  
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True
            ):
        
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "RED")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "#d9d9d9")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "RED")
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "#d9d9d9")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "RED")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "#d9d9d9")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "RED")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        fill_color = "GRAY" if undo else "RED"


        middle_self = Point(int(self._x1 + (self._x2 - self._x1) // 2), int(self._y1 + (self._y2 - self._y1) // 2))
        middle_to_cell = Point(int(to_cell._x1 + (to_cell._x2 - to_cell._x1) // 2), int(to_cell._y1 + (to_cell._y2 - to_cell._y1) // 2))


        self._win.draw_line(Line(middle_self, middle_to_cell), fill_color)
        
