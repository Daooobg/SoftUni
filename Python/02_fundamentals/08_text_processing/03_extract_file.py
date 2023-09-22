file_path = input().split('\\')

file = file_path[-1]

file_name, file_extension = file.split('.')

print(f'File name: {file_name}\nFile extension: {file_extension}')