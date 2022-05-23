current_text = input()
chars_dict = {}

for char in current_text:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1

chars_dict = sorted(chars_dict.items(), key=lambda x: x[0])

for key, value in chars_dict:
    print(f"{key}: {value} time/s")
