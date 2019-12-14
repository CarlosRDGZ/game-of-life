import unittest
from main import *


class TestCreateCells(unittest.TestCase):

    def testNoRowsNColumns(self):
        self.assertListEqual(create_cells(0, 0), [], "Should be empty list")
        self.assertListEqual(create_cells(0, 1), [], "Should be empty list")
        self.assertListEqual(create_cells(0, 2), [], "Should be empty list")

    def testNot0Rows0Columns(self):
        self.assertListEqual(create_cells(1, 0), [[]], "Should be list of one empty list")
        self.assertListEqual(create_cells(2, 0), [[], []], "Should be list of two empty list")

    def testNot0RowsNot0Columns(self):
        self.assertListEqual(create_cells(1, 1), [[False]], "Should be list of a list with one element")
        self.assertListEqual(create_cells(2, 2), [[False, False], [False, False]],
                             "Should be list of two lists of two elements each")


class TestCountNeighbors(unittest.TestCase):

    def testOneCenterIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(4, 4, cells), 0, "Should be 0")

    def testOnCenterSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(3, 6):
            for col in range(3, 6):
                cells[row][col] = True
        self.assertEqual(get_number_of_neighbors(4, 4, cells), 8, "Should be 8")

    def testOnLeftUpperCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(0, 0, cells), 0, "Should be 0")

    def testOnLeftUpperCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(0, 2):
            for col in range(0, 2):
                cells[row][col] = True
        self.assertEqual(get_number_of_neighbors(0, 0, cells), 3, "Should be 3")

    def testOnLeftLowerCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(9, 0, cells), 0, "Should be 0")

    def testOnLeftLowerCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(8, 10):
            for col in range(0, 2):
                cells[row][col] = True
        self.assertEqual(get_number_of_neighbors(9, 0, cells), 3, "Should be 3")

    def testOnRightUpperCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(0, 9, cells), 0, "Should be 0")

    def testOnRightUpperCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(0, 2):
            for col in range(8, 10):
                cells[row][col] = True
        self.assertEqual(get_number_of_neighbors(0, 9, cells), 3, "Should be 3")

    def testOnRightLowerCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(9, 9, cells), 0, "Should be 0")

    def testOnRightLowerCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(8, 10):
            for col in range(8, 10):
                cells[row][col] = True
        self.assertEqual(get_number_of_neighbors(9, 9, cells), 3, "Should be 3")


class TestCellState(unittest.TestCase):

    def testCellIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(should_live(0, 0, cells), False, "Should stay dead")
        cells[0][0] = True
        self.assertEqual(should_live(0, 0, cells), False, "Should die")

    def testNextToOne(self):
        cells = create_cells(10, 10)
        cells[0][1] = True
        self.assertEqual(should_live(0, 0, cells), False, "Should stay dead")
        cells[0][0] = True
        self.assertEqual(should_live(0, 0, cells), False, "Should die")

    def testNextToTwo(self):
        cells = create_cells(10, 10)
        cells[0][1] = True
        cells[1][0] = True
        self.assertEqual(should_live(0, 0, cells), False, "Should stay dead")
        cells[0][0] = True
        self.assertEqual(should_live(0, 0, cells), True, "Should stay alive")

    def testNextToThree(self):
        cells = create_cells(10, 10)
        cells[0][1] = True
        cells[1][0] = True
        cells[1][1] = True
        self.assertEqual(should_live(0, 0, cells), True, "Should born")
        cells[0][0] = True
        self.assertEqual(should_live(0, 0, cells), True, "Should stay alive")

    def testNextToMoreThanThree(self):
        cells = create_cells(10, 10)
        cells[0][0] = True
        cells[0][1] = True
        cells[0][2] = True
        cells[1][0] = True
        self.assertEqual(should_live(1, 1, cells), False, "Should stay dead")
        cells[0][0] = True
        self.assertEqual(should_live(1, 1, cells), False, "Should die")
