import itertools


class ItertoolsFunctions:
    def __init__(self):
        pass

    @staticmethod
    def fun_count():
        """
        generates the elements of an iterable indefinitely
        :return:
        """
        for i in itertools.count(0, 2):
            print(i)
            if i > 10:
                break
        """
        0
        2
        4
        6
        8
        10
        12
        """

    @staticmethod
    def fun_cycle():
        """
        1
        2
        3
        1
        2
        3
        1
        2
        3
        1
        :return:
        """
        c = 0
        for item in itertools.cycle([1, 2, 3]):
            print(item)
            c += 1

            if c >= 10:
                break

    @staticmethod
    def fun_accumulate():
        """
        1
        3
        6
        10
        15
        :return:
        """
        data = [1, 2, 3, 4, 5]
        result = itertools.accumulate(data)

        for item in result:
            print(item)

    @staticmethod
    def fun_chain():
        """
        1
        2
        3
        a
        b
        c
        :return:
        """
        li1 = [1, 2, 3]
        li2 = ['a', 'b', 'c']

        for item in itertools.chain(li1, li2):
            print(item)

    @staticmethod
    def fun_combinations():
        """
        (1, 2)
        (1, 3)
        (1, 4)
        (1, 5)
        (2, 3)
        (2, 4)
        (2, 5)
        (3, 4)
        (3, 5)
        (4, 5)
        :return:
        """
        data = [1, 2, 3, 4, 5]
        result = itertools.combinations(data, 2)

        for item in result:
            print(item)

    @staticmethod
    def fun_permutation():
        """
        (1, 2)
        (1, 3)
        (2, 1)
        (2, 3)
        (3, 1)
        (3, 2)
        :return:
        """
        data = [1, 2, 3]
        result = itertools.permutations(data, 2)

        for item in result:
            print(item)


if __name__ == '__main__':
    i = ItertoolsFunctions()

    # i.fun_count()
    # i.fun_cycle()
    # i.fun_accumulate()
    # i.fun_chain()
    # i.fun_combinations()
    i.fun_permutation()
