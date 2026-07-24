#3. Restaurant Billing System
# Develop a Python program that accepts:
# Customer Name
# Three Food Items
# Price of each Item
# Display:
# Ordered Items
# Total Amount
# GST
# Grand Total



name = input("Enter your name : ")
item1 = input("Enter Your first food item : ")
price1 = float(input("Enter price of this item : "))
item2 = input("Enter Your second food item : ")
price2 = float(input("Enter price of this item : "))
item3 = input("Enter Your third food item : ")
price3 = float(input("Enter price of this item : "))

total = price1 + price2 + price3
gst_amt = float(total * (18/100))

print(f''' 
            -----Restaurent------]
    Customer Name : {name}
    Order Number : 45
    -----------------------------------------
    Item\tPrice
    {item1}\t\t{price1}
    {item2}\t\t{price2}
    {item3}\t\t{price3}
    -----------------------------------------
    Total Amount:\t{total}
    GST:\t\t{round(gst_amt,2)}
    Grand Total:\t{total + gst_amt}
 -----------------------------------------
 Thank You!
   
''')
