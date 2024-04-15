def square(n):
    for i in range(n):
        print('*' * n)


def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + (' ' * (n - 2)) + '*')


def left_triangle(n):
    for i in range(n + 1):
        for j in range(i):
            print('*', end='')
        print()


def right_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        print('*' * (i + 1))


def left_downward_triangle(n):
    for i in range(n + 1, 0, -1):
        print('*' * i)


def right_downward_triangle(n):
    for i in range(n):
        print(' ' * i, end='')
        print('*' * (n - i))


def hollow_triangle(n):
    for i in range(n):
        if i in (0, 1, n - 1):
            print('*' * (i + 1))
        else:
            print('*', end='')
            print(' ' * (i - 1), end='')
            print('*')


def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


def hollow_pyramid_pattern(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        # printing start
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print('*', end='')
            else:
                if i == n:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()


def reversed_pyramid_pattern(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


def diamond_star_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


def hollow_diamond(n):
    for i in range(1, n + 1):
        if i == 1:
            print(' ' * (n - 1) + '*')
        elif i == n:
            print('*' + ' ' * (2 * i - 3) + '*')
        else:
            print(' ' * (n - i), end='')
            print('*' + ' ' * (2 * i - 3) + '*')
    # lower half
    for i in range(n - 1, 0, -1):
        if i == 1:
            print(' ' * (n - 1) + '*')
        elif i == n:
            print('*' + ' ' * (2 * i - 3) + '*')
        else:
            print(' ' * (n - i), end='')
            print('*' + ' ' * (2 * i - 3) + '*')


def hour_glass(n):
    for i in range(n, 0, - 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))
    for i in range(2, n + 1):
        print(' ' * (n - i), end='')
        print('*' * (2 * i - 1))


def right_pascal_star_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

    for i in range(n - 1, 0, -1):
        print('*' * i)


def left_pascal_star_pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * i)


# TODO: stud this!
def heart_pattern(n):
    print(' ' + '*' * ((n + 1) // 2) + ' ' * ((n + 2) // 2) + '*' * ((n + 1) // 2) + ' ')
    print('*' * n + ' ' + '*' * n)

    for i in range(n + 1, 0, -1):
        print(' ' * (n - i + 1), end='')
        print('*' * (2 * i - 1))


def heart_pattern2(n):
    # heart pattern

    # upper part of the heart
    for i in range(n // 2, n, 2):
        # print first spaces
        for j in range(1, n - i, 2):
            print(" ", end="")
        # print first stars
        for j in range(1, i + 1, 1):
            print("*", end="")
        # print second spaces
        for j in range(1, n - i + 1, 1):
            print(" ", end="")
        # print second stars
        for j in range(1, i + 1, 1):
            print("*", end="")
        print()

    # lower part
    for i in range(n, 0, -1):
        for j in range(i, n, 1):
            print(" ", end="")
        for j in range(1, i * 2, 1):
            print("*", end="")
        print()


def plus_pattern(n):
    for i in range(n):
        if i == n // 2:
            print('*' * n)
        else:
            print(' ' * (n // 2) + '*' + ' ' * (n // 2))


def cross_pattern(n):
    for i in range(n):
        if i == n // 2:
            print(' ' * (n // 2) + '*')
        else:
            print('*' + ' ' * (n - (i + 2)) + '*')


# square(5)
# hollow_square(5)
# left_triangle(5)
# right_triangle(5)
# left_downward_triangle(5)
# right_downward_triangle(5)
# hollow_triangle(5)
# pyramid_pattern(5)
# hollow_pyramid_pattern(5)
# reversed_pyramid_pattern(5)
# diamond_star_pattern(5)
# hollow_diamond(6)
# hour_glass(5)
# right_pascal_star_pattern(5)
# left_pascal_star_pattern(5)
# heart_pattern2(10)
# plus_pattern(5)
cross_pattern(5)

