def math_operations(*args, **kwargs):
    keys_dict = dict(kwargs)
    counter = 0
    result_to_print = []

    for float_number in args:
        counter += 1

        if counter > 4:
            counter = 1

        if counter == 1:
            keys_dict["a"] += float_number
        elif counter == 2:
            keys_dict["s"] -= float_number
        elif counter == 3:
            if float_number == 0:
                continue
            keys_dict["d"] /= float_number
        elif counter == 4:
            keys_dict["m"] *= float_number
        else:
            counter = 0

    result = sorted(keys_dict.items(), key=lambda x: (-x[1], x[0]))

    for item in result:
        result_to_print.append(f"{item[0]}: {item[1]:.1f}")

    return "\n".join(result_to_print)


# Test code:
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
