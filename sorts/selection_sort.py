# selection sort implementation
def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    user_input = input("Enter number separated by space: ").strip()
    print(type(user_input[0]))
    user_input = [int(x) for x in user_input.split()]
    print(user_input)
    print(type(user_input[0]))


