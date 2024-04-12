def pattern1(size):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    for i in range(size):
        for j in range(i):
            print('*', end=' ')
        print()

    # alternative solution
    for j in range(size):
        print('* ' * j)


def pattern2(size):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(size, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()


def pattern3(size):
    """
    1
    2 2
    3 3 3
    4 4 4 4
    """
    for i in range(size):
        for j in range(i):
            print(i, end=' ')
        print()


def pattern4(size):
    """
    0 1 2 3 4
    0 1 2 3
    0 1 2
    0 1
    0
    """
    for i in range(size, 0, - 1):
        for j in range(i):
            print(j, end=' ')
        print()


def pattern5(size):
    """
    0
    0 1
    0 1 2
    0 1 2 3
    """
    for i in range(size):
        for j in range(i):
            print(j, end=' ')
        print()


def pattern6(size):
    """
    1 1 1 1 1
    2 2 2 2
    3 3 3
    4 4
    5
    """
    for i in range(size, 0, - 1):
        for j in range(i):
            print((size - i) + 1, end=' ')
        print()


def pattern7(size):
    # alternate numbers pattern
    """
    1
    3 3
    5 5 5
    7 7 7 7
    9 9 9 9 9
    """
    num = -1

    for i in range(size + 1):
        for j in range(i):
            print(num, end=' ')
        print()
        num += 2


def pattern8(size):
    # reverse number pattern
    """
    5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1
    :param size: 5
    :return:
    """
    for i in range(size, 0, -1):
        for j in range(i):
            print(i, end=' ')
        print()


def pattern9(size):
    # reverse pyramid numbers
    """
    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1
    :param size: 5
    :return:
    """
    for i in range(1, size + 1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


def pattern10(size):
    # another reverse number pattern
    """
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    :param size: 5
    :return:
    """
    for i in range(size, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


def pattern11(size):
    """
    1
    3 2
    6 5 4
    10 9 8 7
    :param size: 5
    :return:
    """
    start = 1
    stop = 2
    current = stop

    for i in range(2, size + 1):
        for j in range(start, stop):
            current -= 1
            print(current, end=' ')
        print()
        start = stop
        stop += i
        current = stop


def pattern12(size):
    # right-angled triangle pattern of numbers
    """
            1
          1 2
        1 2 3
      1 2 3 4
    """
    for i in range(1, size):
        num = 1
        for j in range(size, 0, -1):
            if j > i:
                print(' ', end=' ')
            else:
                print(num, end=' ')
                num += 1
        print()


if __name__ == '__main__':
    n = 5

    pattern2(n)
