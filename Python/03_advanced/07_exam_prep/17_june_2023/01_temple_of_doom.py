from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = list(map(int, input().split()))

while len(challenges) != 0:
    if not tools or not substances:
        break

    current_tool = tools.popleft()
    current_substance = substances.pop()
    current_result = current_tool * current_substance

    if current_result in challenges:
        challenges.remove(current_result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if challenges:
    print('Harry is lost in the temple. Oblivion awaits him.')
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")

if substances:
    print(f"Substances: {', '.join([str(substance) for substance in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(challenge) for challenge in challenges])}")