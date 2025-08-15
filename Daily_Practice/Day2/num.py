height = input("What's your height?")
weight = input("What is your weight?")
# stores user input

cal_1 = float(height)
cal_2 = int(weight)
# Changes the first code to float data type and Stores
# Changes the second code to int data type and Stores

bmi = cal_2 / (cal_1 * cal_1)
print("Your BMI is: " + str(bmi))
# First line calculates the BMI of the user
# Second line prints the results