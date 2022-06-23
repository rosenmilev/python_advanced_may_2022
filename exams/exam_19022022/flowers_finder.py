from collections import deque

vowels = deque(input().split(" "))
consonants = input().split(" ")
word_found = False
searched_words = {"rose": set("rose"), "tulip": set("tulip"), "lotus": set("lotus"), "daffodil": set("daffodil")}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for word in searched_words:
        if current_vowel in searched_words[word]:
            searched_words[word].remove(current_vowel)
        if current_consonant in searched_words[word]:
            searched_words[word].remove(current_consonant)
        if not searched_words[word]:
            word_found = True
            print(f"Word found: {word}")
            break
    if word_found:
        break

if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
