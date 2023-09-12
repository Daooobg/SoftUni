product_list = input().split(' ')
command_line = input()

while command_line != 'No Money':
    command_line = command_line.split(' ')

    if command_line[0] == 'OutOfStock':
        for index in range(len(product_list)):
            if product_list[index] == command_line[1]:
                product_list[index] = 'None'

    elif command_line[0] == 'Required':
        index = int(command_line[2])
        if index < len(product_list) and (index >= 0):
            product_list[index] = command_line[1]

    elif command_line[0] == 'JustInCase':
        product_list[-1] = command_line[1]

    command_line = input()

for product in product_list:
    if product != 'None':
        print(product, end=' ')
