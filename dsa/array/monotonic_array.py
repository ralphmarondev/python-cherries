def monotonic_array(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1) or all(
        arr[i] >= arr[i + 1] for i in range(len(arr) - 1)
    ))


if __name__ == '__main__':
    print(f'is monotonic: {monotonic_array([1, 2, 3, 4])}')
