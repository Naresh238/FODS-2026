prices = [100, 50, 30]
quantity = [2, 3, 1]

discount_rate = 10
tax_rate = 5

total = 0
for p, q in zip(prices, quantity):
    total += p * q

discount = total * discount_rate / 100
tax = (total - discount) * tax_rate / 100

final_cost = total - discount + tax
print("Total Cost:", final_cost)
