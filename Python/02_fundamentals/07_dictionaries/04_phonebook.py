phone_book = {}

data = input().split('-')
while True:
    if len(data) == 1:
        break

    name, phone_number = data
    phone_book[name] = phone_number

    data = input().split('-')

n = int(data[0])

for _ in range(n):
    name = input()
    if phone_book.get(name):
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')