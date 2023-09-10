input_str = input()

str_list = input_str.split(', ')
reversed_list = list(reversed(str_list))

for index, animal in enumerate(reversed_list):
    if index == 0 and animal == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif animal == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
        break
