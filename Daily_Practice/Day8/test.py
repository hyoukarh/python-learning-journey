# def my_function(usr_name, location):
#     print(f"Welcome to my program {usr_name} from {location}.")
#     print("That's all this program does.")

# usr_answer = input("Do you want to find out what my function does? enter Y or N. ").lower()

# if usr_answer == "y":
#     my_function(usr_name = "Anonymous User", location = "Milwauke")
# elif usr_answer == "n":
#     print("Your loss.")
# else:
#     print("invalid input")

# import math

# def paint_calc(height, width, cover):
#     paint_cans = (height * width) / cover
#     return paint_cans

# test_h = int(input("What is the height of the wall in meters? "))
# test_w = int(input("What is the width of the wall in meters? "))
# coverage = 5

# total_cans = paint_calc(height = test_h, width = test_w, cover = coverage)
# print(f"You'll need {math.ceil(total_cans)} cans of paint.")

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Please enter a number: "))
prime_checker(number = n)
