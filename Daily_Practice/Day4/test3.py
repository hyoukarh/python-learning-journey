import random

names = input("Enter Five names please.\n").split()
random_name = random.randint(0,4)

print(f"{names[random_name]} is paying the bill today!")
