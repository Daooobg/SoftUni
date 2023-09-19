results = {}
submissions = {}

command = input()

while command != 'exam finished':
    command = command.split('-')
    if command[1] != 'banned':
        name, course, points = command
        points = int(points)

        if course in submissions.keys():
            submissions[course] += 1
        else:
            submissions[course] = 1

        if name in results.keys():
            if course in results[name].keys():
                if results[name][course] < points:
                    results[name][course] = points
            else:
                results[name].update({course: points})

        else:
            results[name] = {course: points}
    else:
        if name in results.keys():
            results.pop(name)

    command = input()

if len(results) > 0:
    print('Results:')
    for k, i in results.items():
        points = []
        for course, result in results[k].items():
            points.append(result)

        all_points = ' | '.join(map(str, points))
        print(f'{k} | {all_points}')

if len(submissions) > 0:
    print('Submissions:')
    for k, i in submissions.items():
        print(f'{k} - {i}')
