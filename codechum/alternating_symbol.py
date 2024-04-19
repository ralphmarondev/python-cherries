'''
Sample Output 1

Enter the number of rows: 3
Enter the number of columns: 4
* # * #
* # * #
* # * #
Sample Output 2

Enter the number of rows: 6
Enter the number of columns: 5
* # * # *
# * # * #
* # * # *
# * # * #
* # * # *
# * # * #
Sample Output 3

Enter the number of rows: 5
Enter the number of columns: 5
* # * # *
# * # * #
* # * # *
# * # * #
* # * # *
'''
def printPattern(row, col):
    if col > row:
        for i in range(row):
            print('* # '* (col // 2), end='')    
            if col % 2 != 0:
                print('*',end='')
            print()
        return

    if col == row:
        if col % 2 == 0:
            for i in range(row):
                print('* # ' * (col // 2), end='')
                if col % 2 != 0:
                    print('*', end='')
                print()
            return
        else:
            for i in range(row):
                if i == 1:
                    print('# * ' * (col // 2), end='')
                    print('#', end='')
                elif i % 2 == 0:
                    print('* # ' * (col // 2), end='')
                else:
                    print('# * ' * (col // 2), end='')
        
                if col % 2 != 0:
                    if i == 1:
                        print()
                        continue
                    if i % 2 == 0:
                        print('*', end='')
                    else:
                        print('#', end='')
                print()
            return
            

    for i in range(row):
        if i == 1:
            print('# * ' * (col // 2), end='')
            print('#', end='')
        elif i % 2 == 0:
            print('* # ' * (col // 2), end='')
        else:
            print('# * ' * (col // 2), end='')

        if col % 2 != 0:
            if i == 1:
                print()
                continue
            if i % 2 == 0:
                print('*', end='')
            else:
                print('#', end='')
        print()
        
            
            

row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of columns: '))

printPattern(row, col)