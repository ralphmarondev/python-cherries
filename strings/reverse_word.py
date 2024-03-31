def reverse_word(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


if __name__ == '__main__':
    user_input = input("Enter string: ")

    print(f"Reverse: {reverse_word(user_input)}")
