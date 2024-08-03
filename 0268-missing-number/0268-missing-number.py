class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #take sum and give difference from nlength
        total = (len(nums) * (len(nums) + 1)) // 2
        count = sum(nums)
        return total - count