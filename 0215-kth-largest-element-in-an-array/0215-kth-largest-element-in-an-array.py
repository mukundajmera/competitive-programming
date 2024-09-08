class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]

        # heap = []
        # for idx in nums:
        #     heapq.heappush(heap, -num)

        # while k > 1:
        #     heapq.heappop(heap)
        #     k -= 1
        
        # return -heapq.heappop(heap)