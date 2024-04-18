def gcd_recursive(x, y):
    if y == 0:
        return x
    return gcd_recursive(y, x % y)

x = 5
y = 25

print(f'Gcd recursive: {gcd_recursive(x, y)}')
