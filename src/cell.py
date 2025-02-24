from tkinter import Canvas
from point import Point, Line
from window import Window

class Cell:
    def __init__(self, point1, point2, win, left=True, right=True, top=True, bottom=True):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

        self._win = win

        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "RED")
            
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "RED")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "RED")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "RED")
