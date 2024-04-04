def is_palindrome_traversal(word):
    last = len(word) // 2
    n = len(word)

    return all(word[i] == word[n - i - 1] for i in range(last))


if __name__ == '__main__':
    print(is_palindrome_traversal("maron"))     # False
    print(is_palindrome_traversal("nan"))       # True
