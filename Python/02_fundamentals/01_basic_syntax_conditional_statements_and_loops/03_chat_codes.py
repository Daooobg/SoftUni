number_of_messages = int(input())

for _ in range(number_of_messages):
    current_message_number = int(input())

    if current_message_number == 88:
        print('Hello')
    elif current_message_number == 86:
        print('How are you?')
    elif current_message_number < 88:
        print('GREAT!')
    else:
        print('Bye.')