number_of_students = int(input())

students_grades = {}

for _ in range(number_of_students):
    student_name = input()
    student_grade = float(input())

    if student_name in students_grades:
        students_grades[student_name].append(student_grade)
    else:
        students_grades[student_name] = [student_grade]


for k, i in students_grades.items():
    student_average_grade = sum(i) / len(i)
    if student_average_grade >= 4.5:
        print(f'{k} -> {student_average_grade:.2f}')