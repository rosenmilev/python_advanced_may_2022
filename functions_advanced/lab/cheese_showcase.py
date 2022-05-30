def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for cheese, values in sorted_cheeses:
        result.append(cheese)
        result.extend(sorted(values, reverse=True))
        result = list(map(str, result))
    return "\n".join(result)
