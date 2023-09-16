number_of_people = int(input())
wagons = list(map(int, input().split()))

for index, wagon in enumerate(wagons):
    if wagon < 4:
        empty_space = 4 - wagon

        if number_of_people >= empty_space:
            number_of_people -= empty_space
            wagons[index] += empty_space
        else:
            wagons[index] += number_of_people
            number_of_people = 0

if number_of_people > 0:
    print(f'There isn\'t enough space! {number_of_people} people in a queue!')
else:
    if sum(wagons) / len(wagons) != 4:
        print('The lift has empty spots!')

print(' '.join(list(map(str, wagons))))