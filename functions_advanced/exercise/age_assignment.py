def age_assignment(*args, **kwargs):
    result = []
    result_to_print = []

    for name in args:
        age = kwargs[name[0]]
        result.append([name, age])
    result = sorted(result)
    [result_to_print.append(f"{x[0]} is {x[1]} years old.") for x in result]

    return "\n".join(result_to_print)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))