def loading_bar(num: int):
    if num == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f'{num}% [', end='')
        for _ in range(10):
            if num > 0:
                print('%', end='')
                num -= 10
            else:
                print('.', end='')
        print(']')
        print('Still loading...')


number = int(input())
loading_bar(number)