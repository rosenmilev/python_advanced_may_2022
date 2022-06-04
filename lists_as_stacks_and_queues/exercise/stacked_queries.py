def queries(current_query: str):
    current_query = current_query.split()
    query_number = current_query[0]

    if query_number == "1":
        numbers_stack.append(int(current_query[1]))
    elif numbers_stack:
        if query_number == "2":
            numbers_stack.pop()
        elif query_number == "3":
            print(max(numbers_stack))
        elif query_number == "4":
            print(min(numbers_stack))


n = int(input())
numbers_stack = []

for _ in range(n):
    current_query = input()
    queries(current_query)

print(*reversed(numbers_stack), sep=", ")
