def even_odd_filter(**kwargs):
    def even_or_odd_command(command):
        if command == "odd":
            return lambda x: x % 2 != 0
        elif command == "even":
            return lambda x: x % 2 == 0
    dict_of_nums = {}
    for key, value in kwargs.items():
        dict_of_nums[key] = list(filter(even_or_odd_command(key), value))

    return dict(sorted(dict_of_nums.items(), key=lambda x: x[1], reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
