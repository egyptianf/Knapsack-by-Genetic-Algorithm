# to test for now
from knapsack import Knapsack
from keyboardInput import KeyboardInput
from fileInput import FileInput
from knapsackGA import GA

fileInput = FileInput("input_example.txt")
fileInput.read()
temp_ks = fileInput.knapsacks[0]
ga = GA(temp_ks)
fittest = ga.main()
best_items = fittest.show_items(temp_ks.items)
best_value = 0
for item in best_items:
    item.show()
    best_value += item.value
print(best_value)
