# print a chirstmas tree
height = int(input('Enter the height of the Christmas tree: '))

for i in range(1, height + 1):
    if i == 0:
        print(' ' * (height - i) + '*')
    else:
        print(' ' * (height - i) + '*' * (2 * i - 1))

for i in range(2):
    print(' ' * (height - 2) + '*' * (3))

'''
Enter the height of the Christmas tree: 10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
        ***
        ***
'''