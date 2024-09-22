class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = 0
        heap = []
        while idx < k:
            heapq.heappush(heap, nums[idx])
            idx += 1
        
        for idx in range(k, len(nums)):
            if nums[idx] > heap[0]:
                heapq.heappush(heap, nums[idx])
                heapq.heappop(heap)
        
        return heap[0]
