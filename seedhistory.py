from matchup import Matchup

class SeedHistory:
    def __init__(self):
        self._records = {}
        self._init_records()

    def _init_records(self):
        MAX_SEED = 16
        for seed in range(1, MAX_SEED+1):
            for opponent_seed in range(1, MAX_SEED+1):
                matchup = Matchup(seed, opponent_seed)
                self._records[matchup] = (0,0)

    def record(self, matchup):
        return self._records[matchup]

    def record_win(self, winning_seed, losing_seed):
        matchup = Matchup(winning_seed, losing_seed)
        wins, losses = self._records[matchup]
        self._records[matchup] = (wins+1, losses)
