'''
if positive = shift right
if negative = shift left

Sample Output 1
Enter the number of elements in the array: 5
Enter the elements of the array: 1 2 3 4 5
Enter the number of positions to shift the array: 3
Shifted array: 3 4 5 1 2

Sample Output 2
Enter the number of elements in the array: 6
Enter the elements of the array: 2 5 8 3 6 9
Enter the number of positions to shift the array: 2
Shifted array: 6 9 2 5 8 3
'''
def shift_array(arr, shift):
    size = len(arr)
    shift = shift % size
    # print(shift)

    shifted_array = arr[-shift:] + arr[:-shift]

    return shifted_array


size = int(input('Enter the number of elements in the array: '))
arr = input('Enter the elements of the array: ').split()
shift = int(input('Enter the number of positions to shift the array: '))

shifted_array = shift_array(arr, shift)
for i in shifted_array:
    print(i, end=' ')
