# find triplets with zero-sum
from itertools import combinations


def find_triplets_with_zero_sum(arr):
    li = [i for i in sorted({i for i in combinations(sorted(arr), 3) if not sum(i)})]
    
    return li


if __name__ == '__main__':
    arr = [1, 3, 2, -3, 0, 2, -3, 4]

    print(find_triplets_with_zero_sum(arr))
