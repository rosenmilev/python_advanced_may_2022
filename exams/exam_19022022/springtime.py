def start_spring(**kwargs):
    items = {}
    result = ""
    for key, value in kwargs.items():
        if value not in items:
            items[value] = []
        items[value].append(key)

    for key in items:
        items[key] = sorted(items[key])

    items = sorted(items.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in items:
        result += f"{key}:\n"
        for element in value:
            result += f"-{element}\n"

    return result


# Test code:
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
