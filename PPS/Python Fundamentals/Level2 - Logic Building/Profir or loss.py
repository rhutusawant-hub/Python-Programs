# Accept cost price and selling price and calculate profit or loss.

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit : ₹{profit:.2f}")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss : ₹{loss:.2f}")

else:
    print(f"Invalid input")