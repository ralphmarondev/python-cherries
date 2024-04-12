# single linked list using python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        pass

    def reverse(self):
        pass

    def insert_first(self, data):
        pass

    def insert_last(self, data):
        pass

    def insert_at_pos(self, data):
        pass

    def delete_first(self):
        pass

    def delete_last(self):
        pass

    def delete_at_pos(self):
        pass


if __name__ == '__main__':
    link = LinkedList()
    choices = ['insert-first', 'insert-last', 'insert-at-pos', 'delete-first', 'delete-last', 'delete-at-pos',
               'display', 'reverse']

    print('Choices:')
    for index, item in enumerate(choices):
        print(f"{index + 1}: {item}")

    while True:
        choice = input('Enter choice ~$ ')

        if choice == 1:
            data = int(input('Enter data: '))
            link.
