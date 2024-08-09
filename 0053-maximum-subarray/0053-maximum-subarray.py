class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        current_sum = 0
        for num in nums:
            if current_sum + num < num:
                current_sum = num
            else:
                current_sum += num
            
            max_sum = max(max_sum, current_sum)
        return max_sum