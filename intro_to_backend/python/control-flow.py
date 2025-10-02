# total_items = 500

# discount1 = 20
# discount2 = 50

# if total_items > 200 and total_items < 200:
#     print("Bill is greater than 200 "  
#            "discount of 20 added")
#     total_items = total_items - discount1
# elif total_items > 300:
#     print("Bill above 200 50 discount added")
#     total_items = total_items - discount2
# print("Total cost :"+ str(total_items))
loyalty = True
total_cost = 500

if loyalty and total_cost > 200:
    # 20% dicount
    total_cost = total_cost - (float(total_cost)/ 100)*20

print("Total bill :"+ str(total_cost))


















