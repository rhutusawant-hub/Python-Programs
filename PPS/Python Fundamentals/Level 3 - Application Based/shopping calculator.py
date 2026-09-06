# Create a shopping calculator that accepts five products, their prices, and quantities and calculates the total bill  

products = []
prices = []
quantities = []

for i in range(5):
    product = input(f"Enter product {i + 1}: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products.append(product)
    prices.append(price)
    quantities.append(quantity)

total_bill = 0

for j in range(5):
    total = prices[i] * quantities[i]
    total_bill += total

print(f"Total Bill: ₹{total_bill:.2f}")
