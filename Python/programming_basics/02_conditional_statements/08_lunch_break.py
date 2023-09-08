from math import ceil

name_of_movie = input()
duration_of_episode = int(input())
duration_of_break = int(input())

duration_for_lunch = duration_of_break / 8
duration_for_rest = duration_of_break / 4

duration_of_break -= duration_for_lunch + duration_for_rest

if duration_of_break >= duration_of_episode:
    print(f'You have enough time to watch {name_of_movie} and left with '
          f'{ceil(duration_of_break - duration_of_episode)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name_of_movie}, you need '
          f'{ceil(duration_of_episode - duration_of_break)} more minutes.')