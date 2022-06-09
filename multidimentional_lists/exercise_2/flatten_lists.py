lists_data = [[x for x in y.split() if x] for y in input().split("|")]
result = []

for row in reversed(lists_data):
    result.extend(row)

print(" ".join(result))
