import unittest
from seedhistory import SeedHistory
from matchup import Matchup

class TestSeedHistory(unittest.TestCase):

    def setUp(self):
        self.history = SeedHistory()
        self.matchup = Matchup(1,16)

    def test_record(self):
        record = self.history.record(self.matchup)
        self.assertEqual((0,0), record)

    def test_record_win_adds_win_for_winning_seed(self):
        self.history.record_win(self.matchup.seed, self.matchup.opponent_seed)
        record = self.history.record(self.matchup)
        self.assertEqual((1,0), record)

if __name__ == '__main__':
    unittest.main()
