class CustomStack:
    def __init__(self, max_size: int):
        # List to store stack elements
        self._stack = [0] * max_size
        # List to store increments for lazy propagation
        self._inc = [0] * max_size
        # Current top index of the stack
        self._top = -1

    def push(self, x: int) -> None:
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = x

    def pop(self) -> int:
        if self._top < 0:
            return -1

        # Calculate the actual value with increment
        result = self._stack[self._top] + self._inc[self._top]

        # Propagate the increment to the element below
        if self._top > 0:
            self._inc[self._top - 1] += self._inc[self._top]

        # Reset the increment for this position
        self._inc[self._top] = 0
        self._top -= 1
        return result

    def increment(self, k: int, val: int) -> None:
        if self._top >= 0:
            # Apply increment to the topmost element of the range
            index = min(self._top, k - 1)
            self._inc[index] += val
# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.stack = []
#         self.capacity = maxSize

#     def push(self, x: int) -> None:
#         if len(self.stack) == self.capacity:
#             return
#         self.stack.append(x)

#     def pop(self) -> int:
#         if len(self.stack) == 0:
#             return -1
        
#         return self.stack.pop()
        
#     def increment(self, k: int, val: int) -> None:
#         if len(self.stack) == 0:
#             return
#         idx = 0
#         while k > 0 and idx < len(self.stack):
#             self.stack[idx] += val
#             k -= 1
#             idx += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)