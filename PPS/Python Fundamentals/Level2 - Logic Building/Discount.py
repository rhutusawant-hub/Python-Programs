# Accept marked price and discount percentage and calculate discount and final price.  

marked_price = float(input("Enter marked price: "))
discount_percent = float(input("Enter discount percentage: "))

discount = marked_price * discount_percent / 100
final = marked_price - discount

print(f"""Discount: ₹{discount:.2f}
Final Price: ₹{final:.2f}
      """)
