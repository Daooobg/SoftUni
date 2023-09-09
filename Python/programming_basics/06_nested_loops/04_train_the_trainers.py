number_of_grades = int(input())
input_line = input()

number_of_presentations = 0
total_avg_num_of_presentations = 0


while input_line != 'Finish':
    name_of_presentation = input_line
    total_grade_for_presentation = 0
    for _ in range(number_of_grades):
        current_grade = float(input())
        total_grade_for_presentation += current_grade

    print(f'{name_of_presentation} - {(total_grade_for_presentation / number_of_grades):.2f}.')

    number_of_presentations += 1
    total_avg_num_of_presentations += total_grade_for_presentation / number_of_grades

    input_line = input()

print(f'Student\'s final assessment is {(total_avg_num_of_presentations / number_of_presentations):.2f}.')