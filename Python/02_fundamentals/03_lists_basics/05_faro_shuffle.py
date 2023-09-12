cards = input().split(' ')
number_of_shuffles = int(input())

for _ in range(number_of_shuffles):
    first_deck = cards[:len(cards) // 2]
    second_deck = cards[len(cards) // 2:]
    cards.clear()

    for index in range(len(first_deck)):
        cards.append(first_deck[index])
        cards.append(second_deck[index])

print(cards)

