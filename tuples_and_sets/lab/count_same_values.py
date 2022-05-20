nums = list(map(float, input().split()))
numbers_dict = {}

for n in nums:
    if n not in numbers_dict:
        numbers_dict[n] = 0
    numbers_dict[n] += 1

[print(f"{key} - {value} times") for key, value in numbers_dict.items()]
