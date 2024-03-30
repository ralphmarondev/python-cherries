def bubble_sort_iterative(collection: list) -> list:
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # stop iteration if the collection is sorted.
    return collection


def bubble_sort_recursive(collection: list) -> list:
    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i+1], collection[i]
            swapped = True
    return collection if not swapped else bubble_sort_recursive(collection)


if __name__ == '__main__':
    unsorted = [10, 50, 20, 40, 30]
    print(f"{bubble_sort_iterative(unsorted) = }")

    unsorted = [10, 50, 20, 40, 30]
    print(f"{bubble_sort_recursive(unsorted) = }")
