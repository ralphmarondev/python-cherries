# factorial using memoization
from functools import lru_cache


@lru_cache
def factorial(n: int) -> ValueError | int:
    if n < 0:
        return ValueError('Number should be positive')

    return 1 if n in (0, 1) else n * factorial(n - 1)


if __name__ == '__main__':
    print(f'Factorial: {factorial(5)}')
