command = input().split(' -> ')

companies = {}

while command[0] != 'End':
    company, employee = command

    if company in companies.keys():
        if employee not in companies[company]:
            companies[company].append(employee)
    else:
        companies[company] = [employee]

    command = input().split(' -> ')


for k, i in companies.items():
    print(k)
    for id in i:
        print(f'-- {id}')