student_heights = input("Add students height. ").split()
total_height = 0
num_of_students = 0

if student_heights == False:
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
        total_height += student_heights[n]
        num_of_students += 1
    avg_height = total_height / num_of_students
    print(avg_height)
else:
    print("Please enter student height.")
