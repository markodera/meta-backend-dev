# bill = 175.00

# tax_bill = 15

# total_taxs = (bill * tax_bill)/100

# print("Total taxs:", total_taxs)
# change = round(bill - total_taxs);2
# print("Amout retured:", change)

def calculate_tax(bill, tax_bill):
    return round((bill * tax_bill) / 100.00, 2)
print("Total tax:", calculate_tax(175.00, 15))
print("Total tax:", calculate_tax(164.33, 22))