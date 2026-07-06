print("select your ride:")
print("1. car")
print("2. bike")

choice = int(input("enter your choice:"))

if choice == 1:
    print("what type of car do you want?")
    print("1. hatchback")
    print("2. sedan")

    choice2 = int(input("enter your choice (1 or 2):"))

    if choice2 == 1:
        print("you have selected hatchback")

    elif choice2 == 2:
        print("you have selected sedan")

    else:
        print("invalid choice")


elif choice == 2:
    print("what type of bike do you want?")
    print("1. yamha")
    print("2. electric scooter")

    choice2 = int(input("enter your choice (1 or 2):"))

    if choice2 == 1:
        print("you have selected yamha")

    elif choice2 == 2:
        print("you have selected electric scooter")

    else:
        print("invalid choice")

else:
    print("invalid choice")

    