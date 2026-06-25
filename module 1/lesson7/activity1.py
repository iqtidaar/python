medical_cause = input("do you have a medical cause (y/x):").lower ()

if medical_cause == "y" :
    print("allowed")

else:
    attendance = int (input("enter your attendance"))
    if attendance > 75:
        print("allowed")
    else:
        print("not allowed")  