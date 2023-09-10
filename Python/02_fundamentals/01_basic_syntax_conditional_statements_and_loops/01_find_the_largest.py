number = input()

for i in range(9, -1, -1):

    for j in number:
        if int(i) == int(j):
            print(j, end='')

