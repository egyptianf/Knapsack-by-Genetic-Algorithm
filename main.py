# to test for now
from knapsack import Knapsack
from keyboardInput import KeyboardInput
from fileInput import FileInput
from knapsackGA import GA

fileInput = FileInput("input_example.txt")
fileInput.read()
case = 1
for knapsack in fileInput.knapsacks:
    ga = GA(knapsack)
    fittest = ga.main()
    best_items = fittest.show_items(knapsack.items)
    best_value = 0
    for item in best_items:
        # item.show()
        best_value += item.value
    print("Case: ", case, best_value)
    case += 1
