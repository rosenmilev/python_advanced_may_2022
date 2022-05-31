def negative_vs_positive(numbers):
    sum_of_negatives = 0
    sum_of_positives = 0
    for num in numbers:
        if num > 0:
            sum_of_positives += num
        else:
            sum_of_negatives += num

    if abs(sum_of_negatives) > sum_of_positives:
        return f"""{sum_of_negatives}
{sum_of_positives}
The negatives are stronger than the positives"""

    elif abs(sum_of_negatives) < sum_of_positives:
        return f"""{sum_of_negatives}
{sum_of_positives}
The positives are stronger than the negatives"""


nums = [int(x) for x in input().split(" ")]
print(negative_vs_positive(nums))
