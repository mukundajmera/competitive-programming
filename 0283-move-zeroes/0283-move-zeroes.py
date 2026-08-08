class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_zero = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[next_zero], nums[idx] = nums[idx], nums[next_zero]
                next_zero += 1