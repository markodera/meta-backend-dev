import random
f_name = input("Type the file name: ")
try:
    with open(f_name, "r") as file:
      print(random.choice(f_name))
except FileNotFoundError as e:
    print("ERROR", e)
except Exception as e:
   print("Something went wrong!", e)