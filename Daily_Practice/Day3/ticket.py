print("Welcome to the Pendulum ride!\n")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the Pendulum")
    age = int(input("What's ypur age? "))
    if age < 12:
        bill = 5
        print("Your ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket is $7.")
    elif age >=45 and age <= 55:
        print("You get a free ticket.")
    else:
        bill = 12
        print("Your ticket is $12.")

    take_photo = input("Do you want to take a photo? Enter Y or N. ")
    if take_photo == "Y":
        bill += 3

    print(f"your total bill is: {bill}")

else:
    print("You're no tall enough for this ride")
