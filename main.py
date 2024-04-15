def fibonacci(n):
    first, second = 0, 1
    _sum = 1
    fibo_list = [0, 1]

    for i in range(2, n):
        fibo_list.append(_sum)
        first = second
        second = _sum
        _sum = first + second
    print(fibo_list)
    print(len(fibo_list))


fibonacci(10)
