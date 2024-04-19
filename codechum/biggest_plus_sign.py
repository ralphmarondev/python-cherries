def biggest_plus_sign(arr):
    row = len(arr)
    col = len(arr[0])
    max_size = 0
    center = (-1, -1)

    for i in range(row):
        for j in range(col):
            if arr[i][j] != 0: # start expanding plus sign from cells with other than 0
                size = 1
                while(i - size >= 0 and
                       i + size < row and
                         j - size >= 0 and
                           j + size < col and 
                      arr[i - size][j] == arr[i + size][j] == arr[i][j - size] == arr[i][j + size] == arr[i][j]):
                    
                    size += 1
                if size > max_size:
                    max_size = size
                    center = (i, j)
    return center


if __name__ == '__main__':
    row = int(input('Enter number of rows: '))
    col = int(input('Enter number of columns: '))

    # arr = []
    # for i in range(row):
    #     e = input('').split()
    #     e = list(map(lambda x: int(x), e))
    #     arr.append(e)
    arr = [list(map(int, input().split())) for _ in range(row)]
    
    center = biggest_plus_sign(arr)
    print(f'The biggest plus sign center is at: {center}')
