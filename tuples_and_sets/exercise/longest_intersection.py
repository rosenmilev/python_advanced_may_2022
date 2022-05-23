n = int(input())
longest_intersection = []
for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_set = set([x for x in range(int(first_start), int(first_end) + 1)])
    second_set = set([x for x in range(int(second_start), int(second_end) + 1)])
    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
