def permutation(arr):
    result: list[list[int]] = []

    if len(arr) == 0:
        return [[]]
    for _ in range(len(arr)):
        n = arr.pop(0)
        perm = permutation(arr.copy())
        for p in perm:
            p .append(n)
        result.extend(perm)
        arr.append(n)
    return result


if __name__ == '__main__':
    print(permutation([1, 2, 3]))

