numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
min = numbers[0]
for number in numbers:
    if number > max:
        max = number
    elif number < min:
        min = number
print(max)
print(min)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for item in row:
        print(item)
