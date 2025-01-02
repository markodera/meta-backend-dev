def divide_by(a, b):
    return a / b 
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print("Cannot divide by zero,", e)
except Exception as e:
    print("Something went wrong", e)