age = input("What is your age?")
# Stores the users age

int_age_weeks = int(age) * 52
# Multiplies the users age by the total weeks in a year

max_age = 90
max_weeks = 90 * 52
# multiplies the max age with the number of weeks in a year

weeks_left = max_weeks - int_age_weeks
print(f"you have {weeks_left} left")
# Subtracts the users weeks from the max weeks