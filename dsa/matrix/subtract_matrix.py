def subtract_matrix(x, y):
    if len(x) != len(y) and len(x[0]) != len(y[0]):
        return -1
    result = []

    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            row.append(x[i][j] - y[i][j])
        result.append(row)
    return result


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = subtract_matrix(a, b)
print('Resultant matrix:')
for row in result:
    print(row)
