elevate_people = int(input())
lift_capacity = int(input())

number_of_courses = elevate_people // lift_capacity

if elevate_people % lift_capacity != 0:
    number_of_courses += 1

print(number_of_courses)

