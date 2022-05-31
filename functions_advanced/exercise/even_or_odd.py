def even_odd(*args):
    numbers = args[:len(args) - 1]
    command = args[-1]
    if command == "odd":
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif command == "even":
        return list(filter(lambda x: x % 2 == 0, numbers))
