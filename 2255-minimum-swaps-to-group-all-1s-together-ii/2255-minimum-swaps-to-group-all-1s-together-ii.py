class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #total count of 1
        count = sum(nums)
        #maximum 1 together 
        min_swap = float('inf')
        one_count = nums[0]
        right = 0

        for left in range(len(nums)):
            if left != 0:
                one_count -= nums[left -1]
            
            #window here
            while right - left + 1 < count:
                right += 1
                one_count += nums[right % len(nums)]

            min_swap = min(min_swap, count - one_count)
        return min_swap





##### non sliding window
    # def minSwaps(self, nums: List[int]) -> int:
    #     #total count of 1
    #     count = 0
    #     #maximum 1 together 
    #     max_one = 0
    #     idx = 0
    #     while idx < len(nums):
    #         if nums[idx] == 1:
    #             current = 0
    #             while idx < len(nums) and nums[idx] == 1:
    #                 current += 1
    #                 count += 1
    #                 idx += 1
    #             max_one = max(max_one, current)
    #         else:
    #             idx += 1
    #     return count - max_one


