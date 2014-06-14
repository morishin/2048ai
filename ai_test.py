from ai import simulate_move, Direction
import unittest

class AiTestCase(unittest.TestCase):
  def setUp(self):
    self.case_in_1 = [[2, 0, 2, 0],
                      [0, 0, 0, 0],
                      [2, 0, 2, 0],
                      [0, 0, 0, 0]]

    self.case_in_2 = [[4, 0, 2, 2],
                      [0, 4, 0, 0],
                      [2, 4, 2, 8],
                      [0, 4, 16, 16]]
  def tearDown(self):
    pass

  def test_simulate_move_1(self):
    # up
    case_out = [[4, 0, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    self.assertEqual(simulate_move(self.case_in_1, Direction.up), case_out)

    # down
    case_out = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [4, 0, 4, 0]]
    self.assertEqual(simulate_move(self.case_in_1, Direction.down), case_out)

    # right
    case_out = [[0, 0, 0, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 4],
                [0, 0, 0, 0]]
    self.assertEqual(simulate_move(self.case_in_1, Direction.right), case_out)

    # left
    case_out = [[4, 0, 0, 0],
                [0, 0, 0, 0],
                [4, 0, 0, 0],
                [0, 0, 0, 0]]
    self.assertEqual(simulate_move(self.case_in_1, Direction.left), case_out)

  def test_simulate_move_2(self):
    # up
    case_out = [[4, 8, 4, 2],
                [2, 4, 16, 8],
                [0, 0, 0, 16],
                [0, 0, 0, 0]]
    self.assertEqual(simulate_move(self.case_in_2, Direction.up), case_out)

    # down
    case_out = [[0, 0, 0, 0],
                [0, 0, 0, 2],
                [4, 4, 4, 8],
                [2, 8, 16, 16]]
    self.assertEqual(simulate_move(self.case_in_2, Direction.down), case_out)

    # right
    case_out = [[0, 0, 4, 4], 
                [0, 0, 0, 4], 
                [2, 4, 2, 8], 
                [0, 0, 4, 32]]
    self.assertEqual(simulate_move(self.case_in_2, Direction.right), case_out)

    # left
    case_out = [[4, 4, 0, 0],
                [4, 0, 0, 0],
                [2, 4, 2, 8],
                [4, 32, 0, 0]]
    self.assertEqual(simulate_move(self.case_in_2, Direction.left), case_out)

if __name__ == "__main__":
  unittest.main()

