def naughty_or_nice_list(*args, **kwargs):
    santas_list = []
    commands = []
    nice = []
    naughty = []

    for element in args:
        if type(element) == str:
            commands.append(element)
        else:
            santas_list = element

    for command in commands:
        command = command.split("-")
        number = int(command[0])
        occurrences_of_number = 0
        kid = ()

        for value, key in santas_list:
            if int(value) == number:
                occurrences_of_number += 1
                kid = value, key

        if occurrences_of_number == 1:
            if command[1] == "Naughty":
                naughty.append(kid[1])
                santas_list.remove(kid)
            elif command[1] == "Nice":
                nice.append(kid[1])
                santas_list.remove(kid)
    kid = ()
    for key, value in kwargs.items():
        occurrences_of_name = 0
        for val, k in santas_list:
            if key == k:
                occurrences_of_name += 1
                kid = val, k
        if occurrences_of_name == 1:
            if value == "Nice":
                nice.append(kid[1])
                santas_list.remove(kid)
            elif value == "Naughty":
                naughty.append(kid[1])
                santas_list.remove(kid)

    result = ""
    santa_kids = []
    if nice:
        result += f"Nice: {', '.join(nice)}\n"
    if naughty:
        result += f"Naughty: {', '.join(naughty)}\n"
    if santas_list:
        for key, value in santas_list:
            santa_kids.append(value)
        result += f"Not found: {', '.join(santa_kids)}"

    return result

# Test code:
# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
#
#
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
