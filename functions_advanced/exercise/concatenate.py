def concatenate(*args, **kwargs):
    result = ""
    for string in args:
        result += string

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)

    return result

# Test code:
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
