class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0

        while left < len(nums) and right < len(nums):
            
            # move till next move 
            while left < len(nums) and nums[left] != 0:
                left += 1
            right = left

            while right < len(nums) and nums[right] == 0:
                right += 1
            
            # print(left, right)
            #swap it
            if right != len(nums):
                nums[left], nums[right] = nums[right], nums[left]
            
            left += 1
        
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
        """
            

