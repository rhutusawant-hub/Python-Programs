# Create a Complete Invoice Generator that accepts customer name, three products, quantities, prices, 
# discount percentage, and tax percentage and calculates the final payable amount.  

customer_name = input("Enter customer name: ")

products = []
prices = []
quantities = []

for i in range(3):
    product = input(f"Enter product {i + 1}: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products.append(product)
    prices.append(price)
    quantities.append(quantity)

discount_percentage = float(input("Enter discount percentage: "))
tax_percentage = float(input("Enter tax percentage: "))

subtotal = 0

for i in range(3):
    subtotal += prices[i] * quantities[i]

discount = subtotal * discount_percentage / 100
amount_after_discount = subtotal - discount

tax = amount_after_discount * tax_percentage / 100
final_amount = amount_after_discount + tax

print(f"Final Payable Amount: ₹{final_amount:.2f}")