num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,88,11]
# for loop
count = 0 
# for num in num_list:
#     if num >45:
#         print("Over 45")
#     else:
#      print("Under 45")
#      print(num)
for idx, num in enumerate(num_list):
    count += 1
    if num == 36:    
        print("Number found at position",idx)
        break
print("Value of count:", count)
