def sort_number_from_string(numbers_as_string: str):
    return sorted(int(n) for n in numbers_as_string.split())


str_numbers = input()
print(sort_number_from_string(str_numbers))