word = input()

word = word.lower()

joined_split_list = word.split('sand') + word.split('water') + word.split('fish') + word.split('sun')


print(len(joined_split_list) - 4)