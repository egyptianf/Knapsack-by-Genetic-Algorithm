from knapsack import Knapsack
from item import Item


class FileInput:
    def __init__(self, file_name):
        self.knapsacks = []
        self.file_name = file_name
        self.file = open(file=self.file_name, mode='r')

    def read(self):
        C = self.file.readline()
        print("Number of test cases is C:", C)
        lines = self.file.readlines()
        items_num_flag = True
        knapsack = Knapsack(0, 0)
        template_counter = 0
        for line in lines:
            if line[0] == '\n':
                continue
            if len((line.rstrip()).split()) == 1 and items_num_flag:
                items_num_flag = False
                if knapsack.S != 0:
                    self.knapsacks.append(knapsack)
                del knapsack
                knapsack = Knapsack(0, 0)
                knapsack.N = int(line.rstrip())
                continue
            if len((line.rstrip()).split()) == 1 and not items_num_flag:
                items_num_flag = True
                knapsack.S = int(line.rstrip())
                continue

            # Initialize knapsack items
            line.rstrip()
            weight, value = line.split(' ')
            item = Item(int(weight), int(value))
            knapsack.items.append(item)
        self.knapsacks.append(knapsack)





    def __del__(self):
        self.file.close()
