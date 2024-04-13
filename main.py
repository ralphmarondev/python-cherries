def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for index, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return index
        left_sum += value
    return -1