number_of_searched_books = 0
searched_book = input()

while True:
    current_book = input()

    if current_book == searched_book:
        print(f'You checked {number_of_searched_books} books and found it.')
        break

    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {number_of_searched_books} books.')
        break

    number_of_searched_books += 1