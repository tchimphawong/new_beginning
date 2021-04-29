numbers = [2, 2, 2, 2, 5]
for x in numbers:
    print(x * 'x')

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

