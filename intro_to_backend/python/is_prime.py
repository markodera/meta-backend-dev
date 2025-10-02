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

is_prime(7)
