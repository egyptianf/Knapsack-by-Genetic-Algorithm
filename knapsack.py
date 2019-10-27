from item import Item


class Knapsack:
    def __init__(self, N, S):
        self.N = N
        self.S = S
        self.items = [None] * N

    def show(self):
        print("Number of items:", self.N)
        print("Knapsack size:", self.S)
        print("Knapsack items:")
        for item in self.items:
            item.show()

    def __del__(self):
        del self.items[:]
