number_of_pages = int(input())
pages_read_in_one_hour = int(input())
number_of_days_to_read_the_book = int(input())

total_time_to_read_the_book = number_of_pages / pages_read_in_one_hour
required_hours_per_day = total_time_to_read_the_book / number_of_days_to_read_the_book

print(int(required_hours_per_day))