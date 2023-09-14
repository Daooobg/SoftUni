def decipher(word: str):
    char_word = ''

    if word[:3].isdigit():
        char_word = chr(int(word[:3])) + word[3:]
    else:
        char_word = chr(int(word[:2])) + word[2:]

    if len(char_word) > 2:
        return char_word[0] + char_word[-1] + char_word[2:-1] + char_word[1]
    else:
        return char_word


secret_message = input().split()
decipher_message = [decipher(word) for word in secret_message]
print(' '.join(decipher_message))