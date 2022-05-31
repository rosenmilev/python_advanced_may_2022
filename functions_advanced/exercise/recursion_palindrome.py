def palindrome(word, index):

    if word[index] == word[-(index + 1)]:
        index += 1
        if index == len(word) - 1:
            return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

    return palindrome(word, index)


print(palindrome("petar", 0))
print(palindrome("abcba", 0))
