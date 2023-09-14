def add_lesson(lesson: str, course_schedule: list):
    if lesson not in course_schedule:
        course_schedule.append(lesson)

    return course_schedule


def insert_lesson(lesson: str, index: int, course_schedule: list):
    if lesson not in course_schedule:
        return course_schedule[:index] + [lesson] + course_schedule[index:]

    return course_schedule


def remove_lesson(lesson: str, course_schedule: list):
    if lesson in course_schedule:
        course_schedule.remove(lesson)
        if lesson + '-Exercise' in course_schedule:
            course_schedule.remove(lesson + '-Exercise')

    return course_schedule


def swap_lesson(first_lesson: str, second_lesson: str, course_schedule: list):
    if first_lesson in course_schedule and second_lesson in course_schedule:
        first_index = course_schedule.index(first_lesson)
        second_index = course_schedule.index(second_lesson)
        course_schedule[first_index], course_schedule[second_index] = (course_schedule[second_index],
                                                                        course_schedule[first_index])

        if first_lesson + '-Exercise' in course_schedule and second_lesson + '-Exercise' in course_schedule:
            course_schedule[first_index + 1], course_schedule[second_index + 1] = (course_schedule[second_index + 1],
                                                                           course_schedule[first_index + 1])
        elif first_lesson + '-Exercise' in course_schedule:
            course_schedule.remove(first_lesson + '-Exercise')
            course_schedule.append(first_lesson + '-Exercise')
        elif second_lesson + '-Exercise' in course_schedule:
            course_schedule.remove(second_lesson + '-Exercise')
            course_schedule.insert(first_index + 1, second_lesson + '-Exercise')

    return course_schedule


def exercise_lesson(lesson: str, course_schedule: list):
    if lesson in course_schedule:
        if lesson + '-Exercise' not in course_schedule:
            lesson_index = course_schedule.index(lesson)
            course_schedule.insert(lesson_index + 1, lesson + '-Exercise')
    else:
        course_schedule.append(lesson)
        course_schedule.append(lesson + '-Exercise')

    return course_schedule


lessons_list = input().split(', ')
command = input().split(':')

while command[0] != 'course start':
    action = command[0]
    current_lesson = command[1]
    is_lesson_exist = any(lesson == current_lesson for lesson in lessons_list)
    if action == 'Add':
        lessons_list = add_lesson(current_lesson, lessons_list)
    elif action == 'Insert':
        index = int(command[2])
        lessons_list = insert_lesson(current_lesson, index, lessons_list)
    elif action == 'Remove':
        lessons_list = remove_lesson(current_lesson, lessons_list)
    elif action == 'Swap':
        lessons_list = swap_lesson(current_lesson, command[2], lessons_list)
    elif action == 'Exercise':
        lessons_list = exercise_lesson(current_lesson, lessons_list)

    command = input().split(':')

for index, lesson in enumerate(lessons_list):
    print(f'{index + 1}.{lesson}')

"""
Data Types, Objects, Lists, Lists-Exercise
Add:Databases
Insert:Arrays:0
Exercise:Objects
Remove:Lists
course start

Arrays, Lists, Lists-Exercise, Methods, Methods-Exercise
Swap:Arrays:Methods
Exercise:Databases
Swap:Lists:Databases
Insert:Arrays:0
course start

Arrays, Lists, Lists-Exercise, Methods, Methods-Exercise, Databases
Swap:Arrays:Methods
Exercise:Databases
Swap:Lists:Databases
Insert:Arrays:0
course start

"""