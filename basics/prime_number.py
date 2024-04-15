def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_one_line(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


if __name__ == '__main__':
    n = int(input('Enter number: '))

    print(is_prime(n))
    print(is_prime_one_line(n))
