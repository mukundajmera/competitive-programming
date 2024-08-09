class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[idx] + nums[left] + nums[right]
                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    result.append([nums[idx],nums[left],nums[right]])
                    left += 1
                    #to skip the duplicate
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result
        # nums.sort()
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]: continue
        #     l, r = i+1, len(nums)-1
        #     while l < r:
        #         total = nums[i] + nums[l] + nums[r]
        #         if total == 0:
        #             res.append([nums[i], nums[l], nums[r]])
        #             l, r = l+1, r-1
        #             while l < len(nums) -1 and nums[l] == nums[l-1]:
        #                 l += 1
        #         elif total > 0:
        #             r -= 1
        #         else:
        #             l += 1
        # return res