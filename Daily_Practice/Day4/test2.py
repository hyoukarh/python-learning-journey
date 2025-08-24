import random

print("welcome to coin toss, toss to test your luck.")
random_toss = random.randint(0, 3)

if random_toss == 1:
    print("You got Heads!")
elif random_toss == 0:
    print("You got Tails!")
elif random_toss == 2:
    print("Edge! Your coin is stuck")
else:
    print("Your coin disappeared!")
