def add(**kwargs):
    sum = 0 
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)
print(add(meat= 3.99, fish =2.99, rice = 5.99))