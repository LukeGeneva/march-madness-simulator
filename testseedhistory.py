import unittest
from seedhistory import SeedHistory

class TestSeedHistory(unittest.TestCase):

    def test_record(self):
        history = SeedHistory()
        record = history.record(1,1)
        self.assertEqual((0,0), record)

if __name__ == '__main__':
    unittest.main()
