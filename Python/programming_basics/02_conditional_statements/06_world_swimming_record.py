record_in_seconds = float(input())
distance = float(input())
swimmer_time_for_one_meter = float(input())

extra_time = (distance // 15) * 12.5
total_time_for_swim = distance * swimmer_time_for_one_meter + extra_time


if total_time_for_swim < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time_for_swim:.2f} seconds.')
else:
    print(f'No, he failed! He was {(total_time_for_swim - record_in_seconds):.2f} seconds slower.')