class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_min = 0
        current_max = 0
        max_sum  = -float('inf')
        min_sum = float('inf')
        total_sum = 0
        for idx in range(len(nums)):
            num = nums[idx]
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

            total_sum += num

        if max_sum <= 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)
