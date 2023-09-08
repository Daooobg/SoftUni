exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

if exam_time == arrival_time:
    print('On time')
else:
    time = exam_time - arrival_time

    minutes = abs(time) % 60
    hours = abs(time) // 60
    # minutes = time % 60

    minutes_in_string = ''

    if minutes < 10:
        minutes_in_string = f'0{minutes}'
    else:
        minutes_in_string = f'{minutes}'

    if time < 0:
        print('Late')

        if hours > 0:
            print(f'{hours}:{minutes_in_string} hours after the start')
        else:
            print(f'{minutes} minutes after the start')

    elif time <= 30:
        print('On time')
        print(f'{minutes} minutes before the start')

    else:
        print('Early')

        if hours > 0:
            print(f'{hours}:{minutes_in_string} hours before the start')
        else:
            print(f'{minutes} minutes before the start')