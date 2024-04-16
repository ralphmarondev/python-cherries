# simple matrix with user input
# row = # of horizontal
# col = # of vertical
def matrix_user_input():
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))

    matrix2d = []
    for i in range(row):
        row = []
        for j in range(col):
            ele = int(input(f'Enter element [{i}][{j}]: '))
            row.append(ele)
        matrix2d.append(row)

    for i in matrix2d:
        print(i)


def matrix_fill_with_0():
    row = 3
    col = 4

    li = [[0 for _ in range(row)] for _ in range(col)]
    for i in li:
        print(i)


matrix_fill_with_0()
