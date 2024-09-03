class Solution:
    def removeElement(self, nums: List[int], val: int):
        index = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[index] = nums[idx]
                index += 1
        return index
