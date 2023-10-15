def age_assignment(*args, **kwargs):
    dictionary = {}
    for k in args:
        for kvp in kwargs.items():
            if k[0] == kvp[0]:
                dictionary[k] = kvp[1]

    sorted_dict = {kvp[0]: kvp[1] for kvp in sorted(dictionary.items(), key= lambda kvp: kvp[0])}

    result = ''
    for k, v in sorted_dict.items():
        result += f'{k} is {v} years old.\n'

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
