def find_emoticons(text, start_index):
    index = text.find(':', start_index)

    return index


def print_emoticons(text):
    index = 0
    while index < (len(text)):
        emoticon_index = find_emoticons(text, index)

        if emoticon_index == -1:
            break

        print(text[emoticon_index:emoticon_index + 2])
        index = emoticon_index + 1


text = input()
print_emoticons(text)