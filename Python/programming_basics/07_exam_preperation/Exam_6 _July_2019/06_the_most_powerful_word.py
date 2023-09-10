from math import floor

command_line = input()

powerful_word_name = ''
powerful_word_points = 0

while command_line != 'End of words':

    current_word_points = 0

    for l in range(len(command_line)):
        current_word_points += ord(command_line[l])

    f = command_line[0]

    if (f == 'a' or f == 'e' or f == 'i' or f== 'o' or f == 'u' or f == 'y' or f == 'A' or f == 'E' or f == 'I' or
            f == 'O' or f == 'U' or f == 'Y'):
        current_word_points = current_word_points * len(command_line)
    else:
        current_word_points = floor(current_word_points / len(command_line))

    if current_word_points >= powerful_word_points:
        powerful_word_points = current_word_points
        powerful_word_name = command_line

    command_line = input()

print(f'The most powerful word is {powerful_word_name} - {powerful_word_points}')