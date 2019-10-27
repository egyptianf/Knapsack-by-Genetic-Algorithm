class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def show(self):
        print(self.weight, self.value)
