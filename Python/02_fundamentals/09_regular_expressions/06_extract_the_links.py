import re

pattern = r'((www)\.([a-zA-Z]+(\-?[a-zA-Z0-9]+)*)\.([a-zA-Z]+(\.?[a-zA-Z]+)*))'

while True:
    text = input()
    if not text:
        break

    matches = re.finditer(pattern, text)

    for match in matches:
        print(match.group())