menu = [
    "Espresso",
    "Latte",
    "Cappuccino",
    "Cold Brew",
    "Americano",
    "Mocha",
    "Macchiato",
    "Turkish Coffee"
]
def find_coffee(coffee):
    if coffee[0] == "c" or coffee[0] == "C":
        return coffee
    
# map_coffee = map(find_coffe, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)