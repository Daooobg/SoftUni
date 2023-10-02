n = int(input())
unique_usernames = {input() for _ in range(n) }
print('\n'.join(unique_usernames))