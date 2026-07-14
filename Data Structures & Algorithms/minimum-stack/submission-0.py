class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val, val if val < self.stack[-1][1] else self.stack[-1][1]])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None
