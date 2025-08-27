student_scores = input("Add student scores. ").split()
max_number = 0

if student_scores:
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
        if student_scores[n] >= max_number:
            max_number = student_scores[n]
    print(f"The highest number in the class is: {max_number}")
