first_string = input()
second_string = input()

final_word = ''
prev_word = ''

for i in range(len(first_string)):
    final_word = second_string[:i + 1] + first_string[i + 1:]

    if final_word != first_string and final_word != prev_word:
        print(final_word)
        prev_word = final_word
