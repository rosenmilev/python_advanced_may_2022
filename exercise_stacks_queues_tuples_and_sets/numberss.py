first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]
    sequence = line[1]

    if command == "Add":
        if sequence == "First":
            first_sequence = first_sequence.union([int(x) for x in line[2:]])
        elif sequence == "Second":
            second_sequence = second_sequence.union([int(x) for x in line[2:]])
    elif command == "Remove":
        if sequence == "First":
            first_sequence = first_sequence.difference([int(x) for x in line[2:]])
        elif sequence == "Second":
            second_sequence = second_sequence.difference([int(x) for x in line[2:]])
    elif command == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
