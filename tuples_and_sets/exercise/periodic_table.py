n = int(input())
elements_set = set()

for _ in range(n):
    current_elements = input().split()
    [elements_set.add(element) for element in current_elements]

for el in elements_set:
    print(el)
