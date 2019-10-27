from knapsack import Knapsack
from item import Item


class KeyboardInput:
    def __init__(self):
        self.knapsacks = []

    def read(self):
        C = int(input("Enter the number of test case: "))
        # Loop through the test cases
        for i in range(C):
            print("Test case: " + str(i + 1))
            N = int(input("Enter the number of items: "))
            S = int(input("Enter the size of the knapsack: "))
            print("Enter the item and its value in pairs: ")
            knapsack = Knapsack(N, S)
            item = Item(0, 0)
            for n in range(N):
                weight, value = input("Pair" + str(n + 1) + ":").split()
                item = Item(weight, value)
                knapsack.items.append(item)
            self.knapsacks.append(knapsack)

