def remove_duplicate(_user_input: str) -> str:
    return " ".join(sorted(set(_user_input.split())))


if __name__ == '__main__':
    user_input = input("Enter string: ")

    print(f"Duplicates removed: {remove_duplicate(user_input)}")
