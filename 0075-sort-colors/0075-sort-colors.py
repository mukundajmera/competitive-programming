class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, idx = 0, 0
        right = len(nums) -1 
        while idx <= right:
            # 3 rules
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                idx += 1
                left += 1
            elif nums[idx] == 1:
                idx += 1
            else:                
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1