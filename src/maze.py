from point import Point
from cell import Cell
from time import sleep

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y= cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                top_left = Point(self.x1 + j * self.cell_size_x, self.y1 + i * self.cell_size_y)
                bottom_right = Point(self.x1 + (j + 1) * self.cell_size_x, self.y1 + (i + 1) * self.cell_size_y)
                cell = Cell(top_left, bottom_right, self.win)
                row.append(cell)
            self._cells.append(row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(.05)