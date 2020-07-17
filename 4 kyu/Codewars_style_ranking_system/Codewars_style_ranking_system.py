class User(object):
    MIN_RANK = -8
    MAX_RANK = 8
    rank_vector = [i for i in range(MIN_RANK, MAX_RANK + 1) if i != 0]
    def __init__(self):
        self.rank = self.MIN_RANK
        self.progress = 0
    def inc_progress(self, kata):
        if kata not in self.rank_vector:
            raise ValueError("Not in the specified Range of features")
        if self.rank == self.MAX_RANK:
            progressmeter = 0
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank):
            progressmeter = self.progress + 3
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank) - 1:
            progressmeter = self.progress + 1
        elif self.rank_vector.index(kata) <= self.rank_vector.index(self.rank) - 2:
            progressmeter = self.progress
        elif self.rank == -1 and kata == 1:
            progressmeter = self.progress + 10
        else:
            progressmeter = self.progress + 10 * pow(abs(self.rank_vector.index(kata) - self.rank_vector.index(self.rank)), 2)
        progressIndex = list(divmod(progressmeter, 100))
        self.progress = progressIndex[1]
        self.rank = self.updaterank(progressIndex[0])
        if self.rank == self.MAX_RANK:
            self.progress = 0
        return self.progress
    def updaterank(self, level = 1):
        new_rank_idx = self.rank_vector.index(self.rank) + level
        self.rank = min(self.MAX_RANK + 1, self.rank_vector[new_rank_idx])
        return self.rank