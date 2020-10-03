def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        m = self.stack[-1]
        return m

    def getMin(self) -> int:
        n = self.stack[0]
        for x in self.stack:
            if x<n:
                n = x
        return n
