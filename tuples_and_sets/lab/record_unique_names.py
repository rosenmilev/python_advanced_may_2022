n = int(input())
unique_names = set()

for _ in range(n):
    current_name = input()
    unique_names.add(current_name)

[print(name) for name in unique_names]
