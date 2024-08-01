class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference  = {}
        result = []
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if nums[idx] in difference:
                return [difference[nums[idx]], idx]
            difference[diff] = idx
        return []