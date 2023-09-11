number = int(input())

for f in range(number):
    for s in range(number):
        for t in range(number):
            current_str = chr(97 + f) + chr(97 + s) + chr(97 + t)
            print(current_str)