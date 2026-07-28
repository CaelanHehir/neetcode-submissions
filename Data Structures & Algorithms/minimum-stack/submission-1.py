class MinStack:

    def __init__(self):
        self.values = []
        self.size = -1

    def push(self, val: int) -> None:
        self.values.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.size >= 0:
            self.values = self.values[:self.size]
            self.size -= 1

    def top(self) -> int:
        return self.values[self.size]

    def getMin(self) -> int:
        return min(self.values)
