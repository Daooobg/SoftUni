first_number = int(input())
second_number = int(input())

for number in range(second_number, 0, -1):
    if number % first_number == 0:
        print(number)
        break