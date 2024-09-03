class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        count = 1
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx -1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[index] = nums[idx]
                index += 1

        return index