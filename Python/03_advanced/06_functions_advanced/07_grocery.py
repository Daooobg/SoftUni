def grocery_store(**kwargs):
    sorted_dic = {kvp[0]: kvp[1] for kvp in sorted(kwargs.items(), key= lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))}
    result = ''

    for k, v in sorted_dic.items():
        result += f'{k}: {v}\n'
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
