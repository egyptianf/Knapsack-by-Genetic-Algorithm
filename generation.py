from individual import Individual


class Generation:
    def __init__(self, N):
        self.size = 50
        self.individuals = [Individual(N) for i in range(self.size)]
        self.individual_len = N

    def __getitem__(self, index):
        return Generation(self.individuals[index])

    def show(self):
        for individual in self.individuals:
            individual.show()
