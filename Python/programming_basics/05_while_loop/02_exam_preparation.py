max_poor_grades = int(input())
name_of_problem = input()
total_grades = 0
number_of_grades = 0
current_poor_grades = 0
last_grade = ''


while name_of_problem != 'Enough':
    current_score = int(input())

    if current_score <= 4:
        current_poor_grades += 1

    if current_poor_grades == max_poor_grades:
        break

    total_grades += current_score
    number_of_grades += 1
    last_grade = name_of_problem
    name_of_problem = input()

if max_poor_grades == current_poor_grades:
    print(f'You need a break, {current_poor_grades} poor grades.')
else:
    print(f'Average score: {(total_grades / number_of_grades):.2f}')
    print(f'Number of problems: {number_of_grades}')
    print(f'Last problem: {last_grade}')