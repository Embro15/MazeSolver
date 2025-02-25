import unittest
from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):
    def setUp(self):
        num_rows = 10
        num_cols = 10
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) // num_cols
        cell_size_y = (screen_y - 2 * margin) // num_rows

        self.maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, seed=0)

        # Create a maze with a fixed seed for predictable results
        #self.maze = Maze(10, 10, 0, 0, 10, 10, seed=42)
    
    def test_maze_initialization(self):
        """Test if maze is created with correct dimensions"""
        self.assertEqual(len(self.maze._cells), 10)  # cols
        self.assertEqual(len(self.maze._cells[0]), 10)  # rows

    def test_cell_visited(self):
        """Test if cells are marked as visited after breaking walls"""
        self.maze._break_walls_r(0, 0)  # start breaking walls from top-left
        # Check if starting cell was visited
        self.assertTrue(self.maze._cells[0][0]._visited)
        self.maze._reset_cells_visited()
        self.assertFalse(self.maze._cells[0][0]._visited)

    def test_outer_walls_intact(self):
        """Test if outer walls of maze remain intact"""
        # Check top row has top walls
        for j in range(10):
            self.assertTrue(self.maze._cells[j][0].has_top_wall)
        
        # Check bottom row has bottom walls
        for j in range(10):
            self.assertTrue(self.maze._cells[j][9].has_bottom_wall)
    


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Check entrance
        self.assertFalse(m1._cells[0][0].has_left_wall)
        # Check exit
        self.assertFalse(m1._cells[-1][-1].has_right_wall)
    
    def setUp(self):
        self.cell = Cell(None)  # Pass None as window isn't needed for these tests
    
    def test_cell_initial_state(self):
        """Test initial cell state"""
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)
        self.assertFalse(self.cell._visited)


    


if __name__ == "__main__":
    unittest.main()