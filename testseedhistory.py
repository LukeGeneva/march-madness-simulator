import unittest
from seedhistory import SeedHistory

class TestSeedHistory(unittest.TestCase):

    def test_record(self):
        history = SeedHistory()
        record = history.record(1,1)
        self.assertEqual((0,0), record)

    def test_record_win_adds_win_for_winning_seed(self):
        history = SeedHistory()
        history.record_win(1, 16)
        record = history.record(1, 16)
        self.assertEqual((1,0), record)

if __name__ == '__main__':
    unittest.main()
