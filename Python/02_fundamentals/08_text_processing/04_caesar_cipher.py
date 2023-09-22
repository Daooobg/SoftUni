def encrypt_char(char):
    char_code = ord(char)
    return chr(char_code + 3)

text = input()

encrypted_text_list = list(map(encrypt_char, text))

print(''.join(encrypted_text_list))