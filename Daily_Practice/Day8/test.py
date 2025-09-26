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
