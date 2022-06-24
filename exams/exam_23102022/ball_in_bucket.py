size = 6
matrix = []
result = 0
for i in range(size):
    matrix.append(input().split(" "))

for _ in range(3):
    command = input().split(", ")
    i = int(command[0][1])
    j = int(command[1][0])
    if 0 <= i < size and 0 <= j < size:
        if matrix[i][j] == "B":
            for row in range(size):
                if matrix[row][j].isdigit():
                    result += int(matrix[row][j])
            matrix[i][j] = 0

prize = ""

if 100 <= result <= 199:
    prize = "Football"
elif 200 <= result <= 299:
    prize = "Teddy Bear"
elif result >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {result} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - result} points more to win a prize.")
