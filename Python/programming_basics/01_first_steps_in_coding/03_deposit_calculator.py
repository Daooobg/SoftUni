deposit = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())

annual_interest = deposit * (annual_interest_rate / 100)
interest_for_one_month = annual_interest / 12
total = deposit + (term_of_deposit * interest_for_one_month)

print(total)