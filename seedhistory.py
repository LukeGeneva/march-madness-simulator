class SeedHistory:
    def __init__(self):
        MAX_SEED = 16
        self._records = {}
        for seed in range(1, MAX_SEED+1):
            for opponent_seed in range(1, MAX_SEED+1):
                matchup = self._create_matchup(seed, opponent_seed)
                self._records[matchup] = (0,0)

    def record(self, seed, opponent_seed):
        matchup = self._create_matchup(seed, opponent_seed)
        return self._records[matchup]

    def record_win(self, winning_seed, losing_seed):
        matchup = self._create_matchup(winning_seed, losing_seed)
        wins, losses = self._records[matchup]
        self._records[matchup] = (wins+1, losses)

    def _create_matchup(self, seed, opponent_seed):
        return (seed, opponent_seed)
