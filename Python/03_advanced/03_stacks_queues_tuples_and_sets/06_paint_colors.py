from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}

secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

found_colors = []

while words:
    first_subs = words.popleft()
    second_subs = words.pop() if words else ''

    for color in (first_subs + second_subs, second_subs + first_subs):
        if color in colors:
            found_colors.append(color)
            break

    else:
        for word in (first_subs[:-1], second_subs[:-1]):
            if word:
                words.insert(len(words) // 2, word)

for color in set(secondary_colors.keys()).intersection(found_colors):
    if not secondary_colors[color].issubset(found_colors):
        found_colors.remove(color)

print(found_colors)