numbers = list(map(int, input().split()))
target_sum = int(input())

result = set()
counter = 0

for i1 in range(len(numbers)):
    for i2 in range(i1 + 1, len(numbers)):
        counter += 1
        if numbers[i1] + numbers[i2] == target_sum:
            print(f"{numbers[i1]} + {numbers[i2]} = {target_sum}")
            result.add(f"({numbers[i1]}, {numbers[i2]})")

print(f"Iterations done: {counter}")
[print(value) for value in result]
