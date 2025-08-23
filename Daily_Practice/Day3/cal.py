print("The love calculator is calculating your score ....")
name_1 = input("what's your name? ")
name_2 = input("what's their name? ")
combined_names = name_1 + name_2
lower_combined_names = combined_names.lower()

t = lower_combined_names.count("t")
r = lower_combined_names.count("r")
u = lower_combined_names.count("u")
e = lower_combined_names.count("e")

true_score = t + r + u + e

l = lower_combined_names.count("l")
o = lower_combined_names.count("o")
v = lower_combined_names.count("v")
e = lower_combined_names.count("e")

love_score = l + o + v + e

score = int(str(true_score) + str(love_score))

if score < 10 or score > 90:
  print(f"your score is {score}, you go together like coke and met.")
elif score >= 40 and score <= 50:
  print(f"your score is {score}, you are alright together")
else:
  print(f"your score is {score}")
