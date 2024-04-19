size = int(input('Enter the height of the Christmas tree: '))

for i in range(size):
    for j in range(1): # need nested loop lol
        print(' ' * (size - i - 1), end='')
        print('*' * (2 * i + 1))

for i in range(2):
    print(' ' * (size - 2) + '***')
