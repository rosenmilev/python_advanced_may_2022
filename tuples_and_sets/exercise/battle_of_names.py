n = int(input())
evens_set = set()
odds_set = set()

for current_row in range(1, n + 1):
    name = input()
    current_sum_of_name = 0
    for char in name:
        current_sum_of_name += ord(char)

    current_result = current_sum_of_name // current_row

    if current_result % 2 == 0:
        evens_set.add(current_result)
    else:
        odds_set.add(current_result)

evens_sum = sum(evens_set)
odds_sum = sum(odds_set)

if evens_sum == odds_sum:
    result = evens_set & odds_set
elif odds_sum > evens_sum:
    result = odds_set - evens_set
else:
    result = odds_set ^ evens_set

print(*result, sep=", ")
