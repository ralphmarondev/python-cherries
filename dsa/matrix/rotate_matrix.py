def rotate_matrix_clockwise(matrix):
    # transpose of matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # reverse each row to get the clockwise rotation
    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix


def rotate_matrix_counterclockwise(matrix):
    # transpose matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
    # reverse each column to get the counterclockwise rotation
    rotated_matrix = [row[::-1] for row in transposed_matrix[::-1]]

    return rotated_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# rotate matrix clockwise
print('\nCounterclockwise')
rotated_matrix = rotate_matrix_clockwise(matrix)

for row in rotated_matrix:
    print(row)


# rotate matrix counterclockwise
print('\nCounterclockwise')
rotated_matrix = rotate_matrix_counterclockwise(matrix)

for row in rotated_matrix:
    print(row)
