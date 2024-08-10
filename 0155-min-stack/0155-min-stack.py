class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        if len(self.stack) > 0:
            self.stack.append((val, min(self.stack[-1][1], val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()