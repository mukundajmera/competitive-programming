class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # first = 1
        # count = 1
        # for idx in range(1,len(nums)):
        #     if nums[idx-1] != nums[idx]:
        #         nums[first] = nums[idx]
        #         first += 1
        # return first
        index = 1
        for idx in range(1, len(nums)):
            if nums[idx-1] != nums[idx]:
                nums[index] = nums[idx]
                index += 1
        return index
        