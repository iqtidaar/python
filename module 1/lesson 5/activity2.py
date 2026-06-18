buying_cost = int(input("enter the buying price"))
selling_cost= int(input("enter the selling price"))

amount = selling_cost - buying_cost

if buying_cost>selling_cost:
    print(f"you have {amount} taka loss.")
else:
    print(f"you have {amount}taka profit.")