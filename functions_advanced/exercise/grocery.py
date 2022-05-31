def grocery_store(**kwargs):
    result = []
    sorted_items = sorted(kwargs.items(), key=lambda x: x[0])
    sorted_items = sorted(sorted_items, key=lambda x: (x[1], len(x[0])), reverse=True)

    for product_info in sorted_items:
        result.append(f"{product_info[0]}: {product_info[1]}")

    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
