# Create a shopping bill that accepts the price and quantity of three products and displays the total b

price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of Product 2: "))

price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

total = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
print(f"Total Bill = ₹{total}")