import re

text = input()

pattern = r'\b_([a-zA-Z0-9]+)\b'

result = re.findall(pattern, text)

print(','.join(result))