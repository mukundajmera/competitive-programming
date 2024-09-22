class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            #add in large minHeap
            heapq.heappush(self.large, num)
        else:
            #add in small maxHeap
            heapq.heappush(self.small, -num)
        
        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.large, -value)
        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()