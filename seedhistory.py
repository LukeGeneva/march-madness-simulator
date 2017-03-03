class SeedHistory:
    def __init__(self):
        self._records = {}

    def record(self, seed, opponent_seed):
        matchup = (seed, opponent_seed)
        return self._records[matchup] if matchup in self._records else (0,0)
