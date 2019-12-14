import unittest
import main as game


class TestCreateCells(unittest.TestCase):

    def testNoRowsNColumns(self):
        self.assertListEqual([], game.create_cells(0, 0), "Should be empty list")
        self.assertListEqual([], game.create_cells(0, 1), "Should be empty list")
        self.assertListEqual([], game.create_cells(0, 2), "Should be empty list")

    def testNot0Rows0Columns(self):
        self.assertListEqual([[]], game.create_cells(1, 0), "Should be list of one empty list")
        self.assertListEqual([[], []], game.create_cells(2, 0), "Should be list of two empty list")

    def testNot0RowsNot0Columns(self):
        self.assertListEqual([[False]], game.create_cells(1, 1), "Should be list of a list with one element")
        self.assertListEqual([[False, False], [False, False]], game.create_cells(2, 2),
                             "Should be list of two lists of two elements each")


class TestCountNeighbors(unittest.TestCase):

    def testOneCenterIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(0, game.get_number_of_neighbors(4, 4, cells), "Should be 0")

    def testOnCenterSurrounded(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        for row in range(3, 6):
            for col in range(3, 6):
                cells[row][col] = True
        self.assertEqual(8, game.get_number_of_neighbors(4, 4, cells), "Should be 8")

    def testOnLeftUpperCornerIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(0, game.get_number_of_neighbors(0, 0, cells), "Should be 0")

    def testOnLeftUpperCornerSurrounded(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        for row in range(0, 2):
            for col in range(0, 2):
                cells[row][col] = True
        self.assertEqual(3, game.get_number_of_neighbors(0, 0, cells), "Should be 3")

    def testOnLeftLowerCornerIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(0, game.get_number_of_neighbors(game.ROWS - 1, 0, cells), "Should be 0")

    def testOnLeftLowerCornerSurrounded(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        for row in range(game.ROWS - 2, game.ROWS):
            for col in range(0, 2):
                cells[row][col] = True
        self.assertEqual(3, game.get_number_of_neighbors(game.ROWS - 1, 0, cells), "Should be 3")

    def testOnRightUpperCornerIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(0, game.get_number_of_neighbors(0, game.COLUMNS - 1, cells), "Should be 0")

    def testOnRightUpperCornerSurrounded(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        for row in range(0, 2):
            for col in range(game.ROWS - 2, game.ROWS):
                cells[row][col] = True
        self.assertEqual(3, game.get_number_of_neighbors(0, game.COLUMNS - 1, cells), "Should be 3")

    def testOnRightLowerCornerIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(0, game.get_number_of_neighbors(game.ROWS - 1, game.COLUMNS - 1, cells), "Should be 0")

    def testOnRightLowerCornerSurrounded(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        for row in range(game.ROWS - 2, game.ROWS):
            for col in range(game.ROWS - 2, game.ROWS):
                cells[row][col] = True
        self.assertEqual(3, game.get_number_of_neighbors(game.ROWS - 1, game.COLUMNS - 1, cells), "Should be 3")


class TestCellState(unittest.TestCase):

    def testCellIsolated(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        self.assertEqual(False, game.should_live(0, 0, cells), "Should stay dead")
        cells[0][0] = True
        self.assertEqual(False, game.should_live(0, 0, cells), "Should die")

    def testNextToOne(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        cells[0][1] = True
        self.assertEqual(False, game.should_live(0, 0, cells), "Should stay dead")
        cells[0][0] = True
        self.assertEqual(False, game.should_live(0, 0, cells), "Should die")

    def testNextToTwo(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        cells[0][1] = True
        cells[1][0] = True
        self.assertEqual(False, game.should_live(0, 0, cells), "Should stay dead")
        cells[0][0] = True
        self.assertEqual(True, game.should_live(0, 0, cells), "Should stay alive")

    def testNextToThree(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        cells[0][1] = True
        cells[1][0] = True
        cells[1][1] = True
        self.assertEqual(True, game.should_live(0, 0, cells), "Should born")
        cells[0][0] = True
        self.assertEqual(True, game.should_live(0, 0, cells), "Should stay alive")

    def testNextToMoreThanThree(self):
        cells = game.create_cells(game.ROWS, game.COLUMNS)
        cells[0][0] = True
        cells[0][1] = True
        cells[0][2] = True
        cells[1][0] = True
        self.assertEqual(False, game.should_live(1, 1, cells), "Should stay dead")
        cells[0][0] = True
        self.assertEqual(False, game.should_live(1, 1, cells), "Should die")


if __name__ == '__main__':
    unittest.main()
