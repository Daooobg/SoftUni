def check_symbols(ticket):
    current_symbols = ''
    result = []
    prev_char = ''
    for char in ticket:

        if char == '@' or char == '#' or char == '$' or char == '^':

            if current_symbols:
                if prev_char != char:
                    result.append(current_symbols)
                    current_symbols = char
                    prev_char = char
                else:
                    current_symbols += char
            else:
                prev_char = char
                current_symbols += char
        else:
            if current_symbols:
                result.append(current_symbols)
                current_symbols = ''

    if current_symbols:
        result.append(current_symbols)

    if len(result) > 0:
        return max(result, key=len)

    return result

def check_ticket(ticket):
    ticket = ticket.strip()

    if len(ticket) != 20:
        return 'invalid ticket'
    left_side = check_symbols(ticket[:10])
    right_side = check_symbols(ticket[10:])

    match_symbols = min(left_side, right_side)

    if len(match_symbols) > 0 and left_side[0] != right_side[0]:
        return f'ticket "{ticket}" - no match'
    elif len(match_symbols) == 10:
        return f'ticket "{ticket}" - 10{match_symbols[0]} Jackpot!'
    elif len(match_symbols) < 6:
        return f'ticket "{ticket}" - no match'
    else:
        return f'ticket "{ticket}" - {len(match_symbols)}{match_symbols[0]}'


tickets = input().split(', ')

for ticket in tickets:
    print(check_ticket(ticket))