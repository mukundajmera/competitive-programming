class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        current_sum = 0
        max_size = float('inf')
        while right < len(nums):

            current_sum += nums[right]
            while current_sum >= target:
                max_size = min(max_size, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
            right += 1

        if max_size == float('inf'):
            return 0

        return max_size