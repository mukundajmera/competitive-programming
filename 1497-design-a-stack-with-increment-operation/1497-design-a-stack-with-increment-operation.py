class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.capacity:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        
        return self.stack.pop()
        
    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0:
            return
        idx = 0
        while k > 0 and idx < len(self.stack):
            self.stack[idx] += val
            k -= 1
            idx += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)