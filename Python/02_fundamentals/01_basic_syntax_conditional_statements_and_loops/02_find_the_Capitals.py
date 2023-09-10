string = input()

list_of_strings = []

for i in range(len(string)):
    if string[i].isupper():
        list_of_strings.append(i)

print(list_of_strings)