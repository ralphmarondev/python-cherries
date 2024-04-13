# remove duplicate
def remove_duplicate(s):
    li = [i for i in s]

    print(f'li: {sorted(li)}')
    li = list(set(li))
    print(f'new li: {sorted(li)}')


if __name__ == '__main__':
    word = 'ralphmaron'

    remove_duplicate(word)


