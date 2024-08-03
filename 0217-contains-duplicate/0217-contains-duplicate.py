class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hash tables
        counterN = Counter(nums)
        for value in counterN.values():
            if value > 1:
                return True
        return False
        # #sorting
        # nums.sort()
        # for idx in range(1,len(nums)):
        #     if nums[idx-1] == nums[idx]:
        #         return True
        # return False