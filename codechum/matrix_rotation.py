row_col = input('Enter the number of rows and columns: ').split()
row_col = [int(i) for i in row_col]
row = row_col[0]
col = row_col[1]

print('Enter the elements of the array:')
arr = []
for i in range(row):
    ele = input('').split()
    ele = [int(i) for i in ele]
    arr.append(ele)

print('Original Matrix:')
for i, row in enumerate(arr):
    for j, num in enumerate(row):
        print(num, end=' ')
    print()

print('Rotated Matrix:')
'''
1 2 3
4 5 6

output:
4 1     => [1][0] [0][0]
5 2     => [1][1] [0][1]
6 3     => [1][2] [0][2]
'''
transposed_matrix = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
rotated_matrix = [i[::-1] for i in transposed_matrix]

for i, row in enumerate(rotated_matrix):
    for j, num in enumerate(row):
        print(num, end=' ')
    print()
