class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 2
        while right >= 0 and nums[right+1] <= nums[right]:
            right -= 1

        if right >= 0:
            left = len(nums) -1

            while nums[left] <= nums[right]:
                left -= 1
            nums[left], nums[right] = nums[right], nums[left]
            
        self.reverse(nums, right + 1)


    #due to inplace
    def reverse(self, nums, index):
        left, right = index, len(nums) -1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1