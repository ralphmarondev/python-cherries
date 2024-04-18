size = int(input('Enter the size of the box: '))

for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' *(size - 2) + '*')
    
'''
Enter the size of the box: 6
* * * * * * 
*         *
*         *
*         *
*         *
* * * * * *
'''