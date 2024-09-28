class MyCircularDeque:

    def __init__(self, k):
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()