class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left, right = 0,0
        # while left < len(nums):
        #     if nums[left] != 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right += 1
        #     left += 1
        zero_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
