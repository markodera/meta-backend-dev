def is_even(start, stop):
    for i in range(start, stop + 1):
        if i % 2 == 0:
            print(i, end=" ")
is_even(1, 20)