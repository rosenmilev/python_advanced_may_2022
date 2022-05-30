def operate(operator, *args):
    def addition():
        return sum(args)

    def subtracting():
        result = args[0]
        for x in args[1:]:
            result -= x
        return result

    def multiply():
        result = args[0]
        for x in args[1:]:
            result *= x

        return result

    def divide():
        result = args[0]
        for x in args[1:]:
            result /= x

        return result

    if operator == "-":
        return subtracting()
    if operator == "+":
        return addition()
    if operator == "*":
        return multiply()
    if operator == "/":
        return divide()


print(operate("*", 3, 4))