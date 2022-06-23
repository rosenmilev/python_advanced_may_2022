def words_sorting(*args):
    word_dict = {}
    ascii_sum = 0
    result = ""
    for word in args:
        if word not in word_dict:
            ascii_value = sum([ord(x) for x in word])
            ascii_sum += ascii_value
            word_dict[word] = ascii_value

    if ascii_sum % 2 == 0:
        word_dict = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        word_dict = sorted(word_dict.items(), key=lambda x: -x[1])

    for word, value in word_dict:
        result += f"{word} - {value}\n"

    return result

# Test code:

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

