class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = idx = 0
        p2 = len(nums) - 1
        while idx <= p2:
            # print(idx, nums[idx], p0, p2, nums)
            if nums[idx] == 0:
                nums[p0], nums[idx] = nums[idx], nums[p0]                
                p0 += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[p2] = nums[p2], nums[idx]
                p2 -= 1
            else:
                idx += 1
    #nums.sort()
        