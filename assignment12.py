#retail store management now wants to provide discount for the bills

b_id = 1001
c_id = 101
b_amount = 200.0
discount_amount = 0
print("b_id: %d" %b_id)
print("Customer_id: %d "%c_id)
print("bill amount:Rs %f" %b_amount)
if((c_id > 100) and (c_id<=1000)) is True:
   if b_amount >= 500:
       discount_amount = b_amount - b_amount * 10/100
       print("discounted bill amount:rs %f" %discount_amount)
   else:
       print("no discount")
else:
    print("Invlaid customer id,Customer id must be between 101 and 1001")
