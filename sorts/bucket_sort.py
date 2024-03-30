def bucket_sort(collection: list, bucket_count: int = 10) -> list:
    if len(collection) == 0 or bucket_count <= 0:
        return []

    min_value, max_value = min(collection), max(collection)
    bucket_size = (max_value - min_value) / bucket_count
    buckets: list[list] = [[] for _ in range(bucket_count)]

    for item in collection:
        index = min(int((item - min_value) / bucket_size), bucket_count - 1)
        buckets[index].append(item)

    return [item for bucket in buckets for item in sorted(bucket)]


if __name__ == '__main__':
    _collection = [10, 50, 20, 40, 30]

    print(f"{bucket_sort(_collection) = }")

