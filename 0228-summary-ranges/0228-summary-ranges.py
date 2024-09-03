class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start = 0
        index = 0
        while index < len(nums):
            while index + 1 < len(nums) and nums[index] + 1 == nums[index + 1]:
                index += 1
            if index == start:                
                result.append(str(nums[index]))
            else:
                result.append(f"{nums[start]}->{nums[index]}")
            index += 1
            start = index
            
        return result



