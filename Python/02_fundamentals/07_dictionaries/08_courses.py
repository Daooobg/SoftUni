command = input()
courses = {}

while command != 'end':
    current_course, current_student = command.split(' : ')

    if current_course in courses.keys():
        courses[current_course].append(current_student)
    else:
        courses[current_course] = []
        courses[current_course].append(current_student)

    command = input()

for k, i in courses.items():
    print(f"{k}: {len(i)}")
    for name in i:
        print(f'-- {name}')
