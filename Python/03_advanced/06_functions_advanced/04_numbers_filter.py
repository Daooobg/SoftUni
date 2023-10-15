def even_odd_filter(**kwargs):
    dictionary = {}
    for kvp in kwargs.items():
        if kvp[0] == 'odd':
            dictionary['odd'] = [num for num in kvp[1] if num % 2 != 0]
        elif kvp[0] == 'even':
            dictionary['even'] = [num for num in kvp[1] if num % 2 == 0]

    sorted_dict = {k: v for k, v in  sorted(dictionary.items(), key=lambda kvp: -len(kvp[1]))}
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
