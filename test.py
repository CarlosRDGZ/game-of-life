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
