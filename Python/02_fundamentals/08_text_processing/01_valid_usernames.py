usernames = input().split(', ')

for username in usernames:
    isValid = True
    if not (3 <= len(username) <= 16):
        isValid = False

    for char in username:
        if char == '_' or char == '-':
            continue

        if not char.isalnum():
            isValid = False

    if isValid:
        print(username)