from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()
    summed_items = first_textile + last_medicament
    if summed_items == 30:
        items["Patch"] += 1
    elif summed_items == 40:
        items["Bandage"] += 1
    elif summed_items == 100:
        items["MedKit"] += 1
    elif summed_items > 100:
        items["MedKit"] += 1
        summed_items -= 100
        medicaments[-1] += summed_items
    else:
        last_medicament += 10
        medicaments.append(last_medicament)

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
