import math

def paint_calc(height, width, cover):
    paint_cans = (height * width) / cover
    return paint_cans

test_h = int(input("What is the height of the wall in meters? "))
test_w = int(input("What is the width of the wall in meters? "))
coverage = 5

total_cans = paint_calc(height = test_h, width = test_w, cover = coverage)
print(f"You'll need {math.ceil(total_cans)} cans of paint.")
