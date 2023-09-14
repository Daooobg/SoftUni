words = input().split()

even_length_words = [word for word in words if len(word) % 2 == 0]

for even_word in even_length_words:
    print(even_word)