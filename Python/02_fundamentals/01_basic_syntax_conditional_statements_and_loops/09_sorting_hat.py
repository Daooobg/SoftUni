input_line = input()

while input_line != 'Welcome!':
    house_name = ''

    if input_line == 'Voldemort':
        print('You must not speak of that name!')
        break

    if len(input_line) < 5:
        house_name = 'Gryffindor.'
    elif len(input_line) == 5:
        house_name = 'Slytherin.'
    elif len(input_line) == 6:
        house_name = 'Ravenclaw.'
    else:
        house_name = 'Hufflepuff.'

    print(f'{input_line} goes to {house_name}')

    input_line = input()

else:
    print('Welcome to Hogwarts.')