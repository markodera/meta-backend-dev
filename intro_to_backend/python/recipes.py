class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.item = items
        self.time = time

    def contents(self):
        print("The"+ self.dish+ "has " +str(self.items)+\
              "and takes " + self.time)