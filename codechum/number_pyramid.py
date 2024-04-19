rows = int(input('Enter the number of rows: '))

for i in range(1, rows + 1):
    # printing spaces
    print(' ' * (rows - i), end='')
    # printing numbers
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
