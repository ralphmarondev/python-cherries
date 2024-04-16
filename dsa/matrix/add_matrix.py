# addition of two matrix
def add_matrix(x, y):
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return -1
    result = []

    # iterate over the row of the matrices
    for i in range(len(x)):
        row = []
        # iterate over the columns of the matrices
        for j in range(len(x[0])):
            # add corresponding elements from A and B
            row.append(x[i][j] + y[i][j])
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

result = add_matrix(a, b)
print('Resultant matrix:')
for row in result:
    print(row)
