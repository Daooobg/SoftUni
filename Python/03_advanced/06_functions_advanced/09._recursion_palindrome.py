def palindrome(word, index=0):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'

    if word[index] == word[len(word) - index - 1]:
        return palindrome(word, index + 1)
    else:
        return f'{word} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
