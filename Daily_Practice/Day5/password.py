import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>', '?', '/', '\\', '|', '`', '~'
]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to password generator.")
num_letters = int(input("How many letters would you like?\n "))
num_symbols = int(input("How many symbols would you like?\n "))
num_numbers = int(input("How many numbers would you like?\n "))

random_password = []
for n in range(num_letters):
    random_password.append(random.choice(letters))

for n in range(num_symbols):
    random_password.append(random.choice(symbols))

for n in range(num_numbers):
    random_password.append(random.choice(numbers))

random.shuffle(random_password)

print(f"Your password is {''.join(random_password)}")
