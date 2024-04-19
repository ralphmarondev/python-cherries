def is_valid_move(matrix, visited, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and not visited[row][col]

def shortest_path(matrix, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(matrix), len(matrix[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = [(start, 0)]

    while queue:
        current, distance = queue.pop(0)
        row, col = current

        if current == end:
            return distance
        
        visited[row][col] = True

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(matrix, visited, new_row, new_col)and matrix[new_row][new_col] != 1:
                queue.append(((new_row, new_col), distance + 1))


if __name__ == '__main__':
    row = int(input('Enter row: '))
    col = int(input('Enter column: '))

    arr = []



