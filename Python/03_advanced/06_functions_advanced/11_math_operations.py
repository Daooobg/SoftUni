from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    operators_dict = {
        'a': lambda num1, num2: num1 + num2,
        's': lambda num1, num2: num1 - num2,
        'd': lambda num1, num2: num1 / num2 if num2 > 0 else num1,
        'm': lambda num1, num2: num1 * num2
    }

    while len(args) > 0:
        for k, v in kwargs.items():
            if len(args) == 0:
                break
            value = float(args.popleft())
            kwargs[k] = operators_dict[k](v, value)

    sorted_dict = {kvp[0]: kvp[1] for kvp in sorted(kwargs.items(), key= lambda kvp: (-kvp[1], kvp[0]))}

    result = ''

    for k, v in sorted_dict.items():
        result += f'{k}: {v:.1f}\n'

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
