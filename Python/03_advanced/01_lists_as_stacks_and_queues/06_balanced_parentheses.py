from collections import deque

brackets= deque(input())

brackets_stack = []

for bracket in brackets:
    if bracket == '{' or bracket == '[' or bracket == '(':
        brackets_stack.append(bracket)
    elif len(brackets_stack) == 0:
        print('NO')
        break
    else:
        prev_bracket = brackets_stack.pop()
        if bracket == '}':
            if prev_bracket != '{':
                print('NO')
                break
        elif bracket == ']':
            if prev_bracket != '[':
                print('NO')
                break
        elif bracket == ')':
            if prev_bracket != '(':
                print('NO')
                break
else:
    print('YES')
