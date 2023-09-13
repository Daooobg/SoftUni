def password_validator(password: str):
    is_valid = True

    if not (6 <= len(password) <= 10):
        print('Password must be between 6 and 10 characters')
        is_valid = False

    password_char_codes = [ord(n) for n in password]

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False

    password_char_numbers = list(filter(lambda num: (47 < num < 58), password_char_codes))
    if len(password_char_numbers) < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')


input_pass = input()
password_validator(input_pass)