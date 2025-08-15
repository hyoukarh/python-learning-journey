print("Hello, welcome to the tip calculator\n")

bill = float(input("What is your bill?\n"))
tip = int(input("Would you like to give a 10, 12, or 15 percent tip?\n"))
num_of_people = int(input("Share bill between how many people?\n"))

cal_tip = (bill / 100) * tip
total_bill = round((bill + cal_tip) / num_of_people, 2)
print(f"Each person should pay {total_bill}")