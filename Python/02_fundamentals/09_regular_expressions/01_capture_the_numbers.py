import re

extracted_numbers = []

while True:
    line = input()
    if not line:
        break

    pattern = r'\d+'

    result = re.findall(pattern, line)
    extracted_numbers.extend(result)

print(' '.join(extracted_numbers))

