class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        index = 0
        result = []
        nums.sort()
        for idx in range(len(nums)-2):
            left = idx + 1
            right = len(nums) - 1
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result