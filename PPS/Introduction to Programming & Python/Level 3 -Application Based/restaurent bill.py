# Create a restaurant bill calculator that accepts food price, quantity, and tax percentage and displays the final bill.

name = input("Enter your name : ")
food_price = float(input("Enter food price: "))
quantity = int(input("Enter quantity: "))
tax_percent = float(input("Enter tax percentage: "))

total = food_price * quantity
tax = total * tax_percent / 100
final = total + tax

print(f"""
    ----------Restaurent----------
    Customer Name : {name}
    Order Number : 45
    ------------------------------
    Food price = {total}
    Quantity = {quantity}
    Tax percentage = {tax_percent}%
    Final amount = {final}
    ------------------------------
      """)