def get_symbols_and_numbers(text):

    current_char = ''
    current_number = ''
    result = []

    for char in text:
        if char.isnumeric():
            current_number += char
            if current_char:
                result.append(current_char)
                current_char = ''
        else:
            current_char += char
            if current_number:
                result.append(current_number)
                current_number = ''
    result.append(current_number)
    return result

def print_repeated_text(text):
    arr = get_symbols_and_numbers(text)
    result = [arr[n].upper() * int(arr[n + 1]) for n in range(0, len(arr), 2)]

    return ''.join(result)


text = input()

result = print_repeated_text(text)
unique_symbols = len(set(result))

print(f'Unique symbols used: {unique_symbols}')
print(result)
