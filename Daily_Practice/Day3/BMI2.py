print("Welcome to BMI calculator 2.0\n")
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))

cal_bmi = weight / (height * height)
if cal_bmi < 18.5:
    print(f"Your BMI is:{cal_bmi} and you're underweight")
elif cal_bmi >= 18.25 and cal_bmi < 25:
    print(f"Your BMI is:{cal_bmi} and you're normalweight")
elif cal_bmi >= 25 and cal_bmi < 30:
    print(f"Your BMI is:{cal_bmi} and you're slightly overweight")
elif cal_bmi >= 30 and cal_bmi < 35:
    print (f"Your BMI is:{cal_bmi} and you're obese")
else:
    print(f"Your BMI is:{cal_bmi} and you're clinically obese")
