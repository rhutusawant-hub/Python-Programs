print("===== E-COMMERCE CHECKOUT =====")
username = input("Enter your username : ")
password = input("Enter you password : ")
if username == "User":
    if password == "User2108":
        print("Login Successfull!")
        membership = input("Enter membership type (GOLD/PLATINUM/SILVER) : ")
        cart_amt = float(input("Enter your cart amount : "))
        if membership == "GOLD":
            discount = cart_amt * 0.15
            final_amount = cart_amt - discount
        elif membership == "PlATINUM":
            discount = cart_amt * 0.10
            final_amount = cart_amt - discount
        elif membership == "SILVER":
            discount = cart_amt * 0.05
            final_amount = cart_amt - discount
        else:
            print("Invalid Membership input.")

        print(f"Discount : ₹ {discount}")
        print(f"Amount after discount : ₹ {final_amount}")

        print("""
        ==========PAYMENT METHODS==========
        1.COD
        2.UPI
        3.Debit Card
        ===================================
        """)
        ch = int(input("Enter your choice : "))

        match ch:
            case 1:
                if final_amount <= 5000:
                    print("Cash on Delivery available!")
                    payment_status = "Pay on Delivery"
                else:
                    print("Cash on Delivery is not available for orders above ₹5000.")
                    payment_status = "Failed"
                   
            case 2:
                upi = input("Enter your upi id : ")
                if "@" in upi:
                    print("UPI Payment Successfull!!")
                    payment_status = "Paid"
                else:
                    print("Invalid UPI Id:(")
                    payment_status = "Failed"

            case 3:
                debit_no = int(input("Enter your debit card number : "))
                if len(debit_no) == 16:
                    print("Payment Successfull")
                    payment_status = "Paid"
                else:
                    print("")
                    payment_status = "Failed"

        print(f"""
        ===== ORDER SUMMARY =====
        Customer : {username}
        Membership : {membership}
        Cart Amount : {cart_amt}
        Discount : {discount}        
        Final Amount : {final_amount}
        Payment Status :  {payment_status}
        ============================
""")
    else:
        print("Incorrect password")
else:
    print("Invalid username!")
