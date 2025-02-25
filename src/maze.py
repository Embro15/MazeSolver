from point import Point
from cell import Cell
from time import sleep
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        if seed is not None:
            random.seed(seed)
        self._x1 = int(x1)
        self._y1 = int(y1)
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = int(cell_size_x)
        self._cell_size_y= int(cell_size_y)
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()


    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(.004)

    def _break_entrance_and_exit(self):
        fc = self._cells[0][0]
        fc.has_left_wall = False
        fc.draw(fc._x1, fc._y1, fc._x2, fc._y2)
        lc = self._cells[-1][-1]
        lc.has_right_wall = False
        lc.draw(lc._x1, lc._y1, lc._x2, lc._y2)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1, j))
            if i < self._num_cols - 1 and not self._cells[i+1][j]._visited:
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i, j-1))
            if j < self._num_rows - 1 and not self._cells[i][j+1]._visited:
                to_visit.append((i, j+1))
            if not to_visit:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            next_i, next_j = to_visit[direction]
            if next_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif next_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif next_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif next_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        for n_i, n_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            
            if 0 <= n_i < self._num_cols and 0 <= n_j < self._num_rows and not self._cells[n_i][n_j]._visited:
                if n_i == i - 1 and self._cells[i][j].has_left_wall:
                    continue
                if n_i == i + 1 and self._cells[i][j].has_right_wall:
                    continue
                if n_j == j - 1 and self._cells[i][j].has_top_wall:
                    continue
                if n_j == j + 1 and self._cells[i][j].has_bottom_wall:
                    continue

                self._cells[i][j].draw_move(self._cells[n_i][n_j])

                if self._solve_r(n_i, n_j):
                    return True
                
                self._cells[i][j].draw_move(self._cells[n_i][n_j], undo=True)
        return False

                
                


