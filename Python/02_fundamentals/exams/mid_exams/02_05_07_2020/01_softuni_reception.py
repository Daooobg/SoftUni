first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

number_of_students = int(input())

number_of_students_helped_for_hour = first_employee + second_employee + third_employee
time = 0
# breaks = 0

while number_of_students != 0:
    time += 1
    if time % 4 == 0:
        continue

    if number_of_students_helped_for_hour <= number_of_students:
        number_of_students -= number_of_students_helped_for_hour
    else:
        number_of_students = 0

print(f'Time needed: {time}h.')