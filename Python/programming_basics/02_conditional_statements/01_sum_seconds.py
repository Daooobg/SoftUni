time_for_first_runner = int(input())
time_for_second_runner = int(input())
time_for_third_runner = int(input())

total_time = time_for_first_runner + time_for_second_runner + time_for_third_runner

minutes = int(total_time / 60)
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
