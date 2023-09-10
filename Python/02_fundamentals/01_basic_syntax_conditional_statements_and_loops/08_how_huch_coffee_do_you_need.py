command_line = input()

total_coffees = 0

while command_line != 'END':
    if (command_line.lower() == 'coding' or command_line.lower() == 'dog' or command_line.lower() == 'cat' or
            command_line.lower() == 'movie'):

        if command_line.islower():
            total_coffees += 1
        elif command_line.isupper():
            total_coffees += 2

    if total_coffees > 5:
        print('You need extra sleep')
        break

    command_line = input()

else:
    print(total_coffees)