actor_name = input()
academy_points = float(input())
number_of_examiners = int(input())

for _ in range(number_of_examiners):
    examiner_name = input()
    examiner_points = float(input())

    academy_points += len(examiner_name) * examiner_points / 2

    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(1250.5 - academy_points):.1f} more!')