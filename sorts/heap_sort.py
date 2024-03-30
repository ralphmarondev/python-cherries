def heapify(collection: list, index: int, heap_size: int):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and collection[left_index] > collection[largest]:
        largest = left_index

    if right_index < heap_size and collection[right_index] > collection[largest]:
        largest = right_index

    if largest != index:
        collection[largest], collection[index] = collection[index], collection[largest]
        heapify(collection, largest, heap_size)


def heap_sort(collection: list):
    length = len(collection)
    for i in range(length // 2 - 1, -1, -1):
        heapify(collection, i, length)
    for i in range(length - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        heapify(collection, 0, i)
    return collection


if __name__ == '__main__':
    _collection = [10, 50, 20, 40, 30]

    print(heap_sort(_collection))
