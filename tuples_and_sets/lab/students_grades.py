number_of_students = int(input())
students_grades = {}

for _ in range(number_of_students):
    current_student = input().split()
    student_name = current_student[0]
    student_grade = current_student[1]

    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(f"{float(student_grade):.2f}")

[print(f"{key} -> {' '.join(value)} (avg: {sum(list(map(float, value))) / len(value):.2f})")
 for key, value in students_grades.items()]
