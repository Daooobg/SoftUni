input_string = input().split()

while True:
    command_line = input().split()
    if command_line[0] == '3:1':
        break

    action = command_line[0]

    if action == 'merge':
        start_index = int(command_line[1])
        end_index = int(command_line[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(input_string):
            end_index = len(input_string) - 1

        merged = ''.join(input_string[start_index:end_index + 1])
        input_string[start_index:end_index+1] = [merged]

    if action == 'divide':
        index = int(command_line[1])
        partitions = int(command_line[2])

        element = input_string[index]
        partition_size = len(element) // partitions
        remaining_chars = len(element) % partitions

        if remaining_chars:
            divided = [element[i:i + partition_size] for i in range(0, len(element) - remaining_chars, partition_size)]
            divided[-1] += element[-remaining_chars:]
        else:
            divided = [element[i:i + partition_size] for i in range(0, len(element), partition_size)]

        input_string.pop(index)
        input_string[index:index] = divided

print(' '.join(input_string))