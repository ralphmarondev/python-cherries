# multiply matrices
def multiply_matrix(x, y):
    if len(x[0]) != len(y):
        return -1

    result = []

    # iterate over the rows of x
    for i in range(len(x)):
        row = []
        # iterate over the column of y
        for j in range(len(y[0])):
            # multiply the elements of the i-th row of x and with the
            # j-th column of y and sum up the result
            total = 0
            for k in range(len(y)):
                total += x[i][k] * y[k][j]
            row.append(total)
        result.append(row)

    return result


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = multiply_matrix(a, b)
for row in result:
    print(row)
