target = int(input("Enter a number between 0 and 500. "))

sum_of_even_numbers = 0
for number in range(0, target + 1):
    if number % 2 == 0:
        sum_of_even_numbers += number


print(sum_of_even_numbers)
