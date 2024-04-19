'''
Sample Output 1

Enter the number of sailors: 3
*   *
 * *
  *
 * *
*   *
Sample Output 2

Enter the number of sailors: 5
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
Sample Output 3

Enter the number of sailors: 7
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *
     * *
    *   *
   *     *
  *       *
 *         *
*           *
'''

n = int(input('Enter the number of sailors: '))

for i in range(2*n - 1): 
    for j in range(2 *n -1):
        if j == i or j == (2* n - 2) - i:
            print('*', end='')
        else:
            print(' ',end='')
    print()


