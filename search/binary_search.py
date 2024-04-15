# binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = input('Enter array separated by space: ').split()
    arr = [int(i.strip()) for i in arr]

    search = int(input('Enter element to search: '))

    if binary_search(arr, search) == -1:
        print('Element is not present in array')
    else:
        print(f'Element is present at index: {binary_search(arr, search)}')
