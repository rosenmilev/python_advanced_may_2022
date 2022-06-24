def shopping_list(budget, **kwargs):
    products_bought = 0
    result = ""

    if budget < 100:
        result = "You do not have enough budget."
    else:
        for key, value in kwargs.items():
            if products_bought == 5:
                break
            current_product = key
            price = float(value[0])
            quantity = int(value[1])
            sum_needed = price * quantity
            if sum_needed <= budget:
                products_bought += 1
                budget -= sum_needed
                result += f"You bought {current_product} for {sum_needed:.2f} leva.\n"

    return result

# Test Code
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print()
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
# print()
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
