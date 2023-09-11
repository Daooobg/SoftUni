number = int(input())

for num in range(2, number):
    if number % num == 0:
        print('False')
        break
else:
    print('True')