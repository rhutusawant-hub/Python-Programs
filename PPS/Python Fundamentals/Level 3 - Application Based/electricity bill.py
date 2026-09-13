# Create an electricity bill calculator using units consumed and price per unit.  

units = float(input("Enter units consumed: "))
price_per_unit = float(input("Enter price per unit: "))

bill = units * price_per_unit

print(f"Electricity Bill: ₹{bill:.2f}")