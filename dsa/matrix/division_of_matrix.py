# Division of matrix
def matrix_multiplication(x, y):
    # check if can be multiplied
    if len(x[0]) != len(y):
        return -1

    # initialize an empty matrix to store the result
    result = [[0] * len(y[0]) for _ in range(len(x))]

    # perform matrix multiplication
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result


# calculate the inverse of matrix b
def matrix_inverse(x):
    n = len(x)

    # create an identity matrix of the same size as x
    identity = [[0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1

    # Gaussian elimination
    for i in range(n):
        # make the diagonal element non-zero
        if x[i][i] == 0:
            for j in range(i + 1, n):
                if x[j][i] != 0:
                    x[i], x[j] = x[j], x[i]
                    identity[i], identity[j] = identity[j], identity[i]
                    break

        # make the diagonal element 1
        if x[i][i] != 1:
            divisor = a[i][i]
            for j in range(n):
                x[i][j] /= divisor
                identity[i][j] /= divisor

        # eliminate the non-diagonal elements
        for j in range(n):
            if i != j and x[j][i] != 0:
                multiplier = x[j][i]
                for k in range(n):
                    x[j][k] -= multiplier * x[i][k]
                    identity[j][k] -= multiplier * identity[i][k]

    return identity


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

inverse_b = matrix_inverse(b)

# multiply matrix a by inverse of b
result = matrix_multiplication(a, inverse_b)

print('Result of A divided by B:')
for row in result:
    print(row)

# how does this work? lol
