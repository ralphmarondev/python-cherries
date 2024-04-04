# remove duplicates
def remove_duplicates(_list: list) -> str:
    return " ".join(set(_list))


if __name__ == '__main__':
    n = input("Enter collection: ").split()

    print(f"After removing obstacles: {remove_duplicates(n)}")
