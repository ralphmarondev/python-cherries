def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True


_sum = 0
while True:
    n = int(input('Enter number: '))

    if n < 0:
        break

    if is_prime(n):
        _sum += n

print(f'Sum of prime numbers: {_sum}')
