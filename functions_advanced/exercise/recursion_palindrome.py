def palindrome(word, index):
    if word[index] == word[-(index + 1)]:
        if index == len(word) // 2:
            return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


# Test code:
# print(palindrome("abcba", 0))
# print(palindrome("abцьзcba", 0))
