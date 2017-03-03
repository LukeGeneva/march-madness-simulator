class Matchup:

    def __init__(self, seed, opponent_seed):
        self.seed = seed
        self.opponent_seed = opponent_seed

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.seed, self.opponent_seed))

    def reverse(self):
        return Matchup(self.opponent_seed, self.seed)
