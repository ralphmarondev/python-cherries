def is_palindrome_traversal(word):
    last = len(word) // 2
    n = len(word)

    return all(word[i] == word[n - i - 1] for i in range(last))


def is_palindrome_recursive(word):
    if len(word) <= 2:
        return True
    if word[0] == word[len(word) - 1]:
        return is_palindrome_recursive(word[1:-1])
    else:
        return False


def is_palindrome_slice(word):
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome_traversal("maron"))     # False
    print(is_palindrome_traversal("nan"))       # True

    print(is_palindrome_recursive("maron"))     # False
    print(is_palindrome_recursive("nan"))       # True

    print(is_palindrome_slice("maron"))     # False
    print(is_palindrome_slice("nan"))       # True
