def even_odd(*args):
    numbers = args[:len(args) - 1]
    command = args[-1]
    if command == "odd":
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif command == "even":
        return list(filter(lambda x: x % 2 == 0, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
