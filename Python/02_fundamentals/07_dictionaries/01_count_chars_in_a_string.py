text = input().split()

count_chars = {}

for word in text:
    for i in range(len(word)):
        if word[i] in count_chars.keys():
            count_chars[word[i]] += 1
        else:
            count_chars[word[i]] = 1

for k, v in count_chars.items():
    print(f'{k} -> {v}')