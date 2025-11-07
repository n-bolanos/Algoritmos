from math import floor


class HashTableChaining():
    def __init__(self, m: int, A: float) -> None:
        self.data: list[None | list[int]] = [None for _ in range(m)]
        self.size = m
        self.alpha = A

    def hashing(self, key: int) -> int:
        return floor(self.size * (key*self.alpha - floor(key*self.alpha)))

    def insert(self, value: int):
        index = self.hashing(value)
        if self.data[index] is None:
            self.data[index] = [value]
        else:
            self.data[index].insert(0, value)  # type: ignore

    def print_table(self):
        for lista in (self.data):
            if lista is not None:
                print(*lista)
            else:
                print("#")


numValues = int(input())
alpha = float(input())
size = int(input())
tabla = HashTableChaining(size, alpha)
for _ in range(numValues):
    value = int(input())
    tabla.insert(value)

tabla.print_table()
