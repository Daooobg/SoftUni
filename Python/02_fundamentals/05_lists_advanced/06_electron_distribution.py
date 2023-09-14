number_of_electrons = int(input())

shell = []
current_shell = 1

while True:
    empty_space = 2 * (current_shell ** 2)
    if empty_space < number_of_electrons:
        shell.append(empty_space)
        number_of_electrons -= empty_space
    elif empty_space >= number_of_electrons:
        shell.append(number_of_electrons)
        break

    current_shell += 1

print(shell)