word = input()

while word != 'End':
    if word != 'SoftUni':
        for i in range(len(word)):
            print(word[i] + word[i], end='')
        print()

    word = input()