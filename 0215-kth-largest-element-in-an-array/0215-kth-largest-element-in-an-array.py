class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if not nums:
            return 
        
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
        
        return heap[0]