'''
write a program that takes a user input array of integers and swaps
every pair of adjacent elements in the array
'''
size = int(input('Enter the size of the array: '))

print('Enter the elements of the array:')
arr = []
for i in range(size):
    e = int(input(''))
    arr.append(e)

print(arr)
# swap every adjacent
new_arr = []
for i in range(0, len(arr) - 1, 2):
    new_arr.append(arr[i + 1])
    new_arr.append(arr[i])

print('The modified array is: ', end='')
for i in new_arr:
    print(i, end=' ')
if size % 2 != 0:
    print(arr[len(arr) - 1])

'''
Enter the size of the array: 5
Enter the elements of the array:
1
2
2
6
5
[1, 2, 2, 6, 5]
The modified array is: 2 1 6 2 5
'''