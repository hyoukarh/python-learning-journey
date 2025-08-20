print("Welcome to imaginative pizza deliveries!")
size = input("What size of pizza do you want? S, M, or L. ")
pepperoni = input("Do you want pepperoni? Y or N. ")
cheese = input("Do you want extra cheese? Y or N. ")
bill = 0

if size == "S":
    bill = 15

    if pepperoni == "Y":
        bill += 2

    if cheese == "Y":
        bill += 1

    print(f"Your total bill is: ${bill}")

elif size == "M":
    bill = 20

    if pepperoni == "Y":
        bill += 2

    if cheese == "Y":
        bill += 1

    print(f"Your total bill is: ${bill}")

else:
    bill = 25

    if pepperoni == "Y":
        bill += 2

    if cheese == "Y":
        bill += 1

    print(f"Your total bill is: ${bill}")
