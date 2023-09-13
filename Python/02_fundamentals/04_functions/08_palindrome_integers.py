def is_palindrome(number: str):
    return number == number[::-1]


input_line = input().split(', ')
for n in input_line:
    print(is_palindrome(n))