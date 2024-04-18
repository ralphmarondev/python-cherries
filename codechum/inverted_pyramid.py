# todo: implement this
size = int(input('Enter the height of the inverted pyramid: '))

# 9 -> 7 -> 5 -> 3 -> 1
for i in range(size, 0, -1):
    if i == size:
        print('*' * (2 * i - 1))
    else:
        print(' ' * (i - size) + '*' * (2 * i - 1))
