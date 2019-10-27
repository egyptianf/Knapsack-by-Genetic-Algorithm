from knapsack import Knapsack
from generation import Generation
from individual import Individual
import random


class GA:
    def __init__(self, knapsack):
        self.knapsack = knapsack
        self.G = 1000  # Number of generations
        self.P_c = 0.4
        self.P_m = 0.001

    def initialize(self):
        g = Generation(self.knapsack.N)
        # Random initialization
        for individual in g.individuals:
            individual.random_initialize(self.knapsack.S, self.knapsack.items)
        return g

    def fitness(self, g):
        items = self.knapsack.items
        for individual in g.individuals:
            individual.calc_fitness(items)

    def sort_individual(self, individual):
        return individual.fitness

    def select_for_reproduction(self, g):
        # Roulette Wheel
        pop_size = g.size
        g.individuals.sort(key=self.sort_individual)
        half = int(pop_size / 2)
        g.individuals = g.individuals[half:]
        return g

    def crossover(self, g):
        locus = random.randint(0, g.individual_len)
        individuals_count = len(g.individuals)
        for j in range(0, individuals_count):
            if len(g.individuals) >= g.size:
                break
            offspring1, offspring2 = g.individuals[j].crossover(g.individuals[j + 1], locus, self.P_c,
                                                                self.knapsack.items, self.knapsack.S, self.P_m)
            g.individuals.append(offspring1)
            g.individuals.append(offspring2)

        # Remove surplus individuals if any
        if len(g.individuals) > g.size:
            g.individuals.remove(g.individuals[g.size])
        return g

    def mutation(self, g):
        items = self.knapsack.items
        for individual in g.individuals:
            individual.mutate(self.P_m, items, self.knapsack.S)
        return g

    def main(self):
        g = self.initialize()
        for i in range(self.G):
            self.fitness(g)
            self.select_for_reproduction(g)
            g = self.crossover(g)
            g = self.mutation(g)

        # NOW we get the fittest individual, need to be updated
        fittest_individual = Individual(self.knapsack.N)

        for individual in g.individuals:
            if (individual.fitness > fittest_individual.fitness) and individual.feasible(self.knapsack.S):
                fittest_individual = individual
        return fittest_individual
