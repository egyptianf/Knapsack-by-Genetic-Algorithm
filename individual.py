import random
from item import Item

class Individual:
    def __init__(self, N):
        self.chromosome = [None] * N
        self.fitness = 0
        self.chromosome_len = N

    def random_initialize(self, S, items):

        for i in range(len(self.chromosome)):
            self.chromosome[i] = random.randint(0, 1)
        self.calc_fitness(items)
        while not self.feasible(S):
            for i in range(len(self.chromosome)):
                self.chromosome[i] = random.randint(0, 1)
            self.calc_fitness(items)


    def show(self):
        print("Chromosome:", self.chromosome, "Fitness:", self.fitness)

    def show_items(self, items):
        best_items = []
        for i in range(self.chromosome_len):
            gene = self.chromosome[i]
            if gene == 1:
                best_items.append(items[i])
        return best_items

    def calc_fitness(self, items):
        self.fitness = 0
        for i in range(self.chromosome_len):
            gene = self.chromosome[i]
            self.fitness += (gene * items[i].weight)

    def feasible(self, S):
        return self.fitness <= S


    def mutate(self, P_m, items, S):
        for i in range(self.chromosome_len):
            r = random.random()
            if r <= P_m:
                self.chromosome[i] ^= 1
        self.calc_fitness(items)

        while not self.feasible(S):
            for i in range(self.chromosome_len):
                r = random.random()
                if r <= P_m:
                    self.chromosome[i] ^= 1
            self.calc_fitness(items)


    def crossover(self, individual, locus, P_c, items, S, P_m):
        N = len(self.chromosome)
        offspring1 = Individual(N)
        offspring2 = Individual(N)
        offspring1.chromosome = self.chromosome.copy()
        offspring1.fitness = self.fitness
        offspring2.chromosome = individual.chromosome.copy()
        offspring2.fitness = individual.fitness

        r = random.random()
        if r <= P_c:
            for i in range(locus + 1, N):
                offspring1.chromosome[i] = individual.chromosome[i]
                offspring2.chromosome[i] = self.chromosome[i]
            offspring1.calc_fitness(items)
            offspring2.calc_fitness(items)

        while not offspring1.feasible(S):
            offspring1.mutate(P_m, items, S)
        while not offspring2.feasible(S):
            offspring2.mutate(P_m, items, S)

        return offspring1, offspring2
