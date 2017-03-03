import unittest
from seedhistory import SeedHistory
from matchup import Matchup

class TestSeedHistory(unittest.TestCase):

    def test_record(self):
        history = SeedHistory()
        matchup = Matchup(1,1)
        record = history.record(matchup)
        self.assertEqual((0,0), record)

    def test_record_win_adds_win_for_winning_seed(self):
        history = SeedHistory()
        matchup = Matchup(1, 16)
        history.record_win(matchup)
        record = history.record(matchup)
        self.assertEqual((1,0), record)

if __name__ == '__main__':
    unittest.main()
