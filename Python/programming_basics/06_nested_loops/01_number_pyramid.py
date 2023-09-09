number = int(input())
current_number = 1
flag = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current_number > number:
            flag = True
            break

        print(str(current_number) + ' ', end='')
        current_number += 1

    if flag:
        break
    print()