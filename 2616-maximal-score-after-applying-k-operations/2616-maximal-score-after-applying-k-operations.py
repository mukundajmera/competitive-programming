class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            largest = -heapq.heappop(nums)
            score += largest
            k -= 1
            heapq.heappush(nums, -(math.ceil(largest / 3)))
        
        return score