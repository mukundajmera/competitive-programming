class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or -self.small[0] >= num:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        #balance the heap lengths
        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        elif len(self.small) < len(self.large):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            small_value = -self.small[0]
            large_value = self.large[0]
            return (small_value + large_value) / 2
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()