class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


if __name__ == '__main__':
    fibo = Fibonacci()

    print(f'Fibonacci: {fibo.get(10)}')
