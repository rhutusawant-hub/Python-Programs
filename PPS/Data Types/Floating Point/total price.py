# Accept the price and quantity of a product and calculate the total price as a decimal value.

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity

print(f"Total Price: {total_price:.2f}")