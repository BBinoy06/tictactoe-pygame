import unittest
import main  # import your variables

class Layout(unittest.TestCase):

    def test_window_size(self):
        self.assertEqual(main.WINDOW_SIZE, 600)

    def test_board_size(self):
        self.assertEqual(main.BOARD_SIZE, 540)

    def test_board_position(self):
        self.assertEqual(main.xboard, (main.WINDOW_SIZE - main.BOARD_SIZE) // 2)
        self.assertEqual(main.yboard, (main.WINDOW_SIZE - main.BOARD_SIZE) // 2)

if __name__ == "__main__":
    unittest.main()
