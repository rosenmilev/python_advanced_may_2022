parentheses_sequence = input()
opening_parentheses = []
not_balanced = False
parentheses_dict = {
    ")": "(",
    "]": "[",
    "}": "{"
}

for symbol in parentheses_sequence:
    if symbol in parentheses_dict.values():
        opening_parentheses.append(symbol)
    elif symbol in parentheses_dict:
        if not opening_parentheses:
            not_balanced = True
            break
        if parentheses_dict[symbol] == opening_parentheses[-1]:
            opening_parentheses.pop()
        else:
            not_balanced = True
            break

if opening_parentheses or not_balanced:
    print("NO")
else:
    print("YES")
