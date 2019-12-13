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


class TestCountNeighbors(unittest.TestCase):

    def testOneCenterIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(4, 4, cells), 0, "Should be 0")

    def testOnCenterSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(3, 6):
            for col in range(3, 6):
                cells[row][col]['isAlive'] = True
        self.assertEqual(get_number_of_neighbors(4, 4, cells), 8, "Should be 8")

    def testOnLeftUpperCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(0, 0, cells), 0, "Should be 0")

    def testOnLeftUpperCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(0, 2):
            for col in range(0, 2):
                cells[row][col]['isAlive'] = True
        self.assertEqual(get_number_of_neighbors(0, 0, cells), 3, "Should be 3")

    def testOnLeftLowerCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(9, 0, cells), 0, "Should be 0")

    def testOnLeftLowerCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(8, 10):
            for col in range(0, 2):
                cells[row][col]['isAlive'] = True
        self.assertEqual(get_number_of_neighbors(9, 0, cells), 3, "Should be 3")

    def testOnRightUpperCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(0, 9, cells), 0, "Should be 0")

    def testOnRightUpperCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(0, 2):
            for col in range(8, 10):
                cells[row][col]['isAlive'] = True
        self.assertEqual(get_number_of_neighbors(0, 9, cells), 3, "Should be 3")

    def testOnRightLowerCornerIsolated(self):
        cells = create_cells(10, 10)
        self.assertEqual(get_number_of_neighbors(9, 9, cells), 0, "Should be 0")

    def testOnRightLowerCornerSurrounded(self):
        cells = create_cells(10, 10)
        for row in range(8, 10):
            for col in range(8, 10):
                cells[row][col]['isAlive'] = True
        self.assertEqual(get_number_of_neighbors(9, 9, cells), 3, "Should be 3")
