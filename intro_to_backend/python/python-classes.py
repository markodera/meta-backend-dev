# class Myclass:
#    def hello(self):
#         print("hello world!")

#    a = 5
# myc = Myclass()
# print(myc.a)
# print(myc.hello())

class Prime():
   def __init__(self, start, stop):
      for i in range(start, stop + 1):
        if i % 2 == 0:
            print(i, end=" ")
      print(" ")

   def is_prime(a):
    if a < 1 :
        print(f"{a} is not a valid number")
        return False
    for i in range(2, int(a**0.5 +1)):
        if a % i == 0:
            print(f"{a} is not a prime number")
            return False
    print(f"{a} is a prime number")
    return True  

Prime(1, 20)
Prime.is_prime(21)