import math
from collections import deque


def calculations(nums, operator, res, is_first):
    if is_first:
        result = int(nums[0])
        if operator == "+":
            for i in range(1, len(nums)):
                result += int(nums[i])
        elif operator == "-":
            for i in range(1, len(nums)):
                result -= int(nums[i])
        elif operator == "*":
            for i in range(1, len(nums)):
                result *= int(nums[i])
        elif operator == "/":
            for i in range(1, len(nums)):
                result = math.floor((result / int(nums[i])))
    else:
        result = res
        if operator == "+":
            for el in nums:
                result += int(el)
        elif operator == "-":
            for el in nums:
                result -= int(el)
        elif operator == "*":
            for el in nums:
                result *= int(el)
        elif operator == "/":
            for el in nums:
                result = math.floor((result / int(el)))
    return result


string = deque(input().split(" "))
operators = "+-*/"
current_numbers = []
first = True
result = 0

while string:
    current_element = string.popleft()
    if current_element in operators:
        result = calculations(current_numbers, current_element, result, first)
        current_numbers = []
        first = False
    else:
        current_numbers.append(current_element)

print(result)
