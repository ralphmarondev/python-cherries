# product sum
def product_sum(arr, depth):
    total_sum = 0

    for i in arr:
        total_sum += product_sum(i, depth + 1) if isinstance(i, list) else i
    return total_sum * depth


if __name__ == '__main__':
    arr = [1, 2, [3]]
    # 1 + 2 + 2(3)

    print(f'Product sum: {product_sum(arr, 1)}')

