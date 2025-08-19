class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for idx in range(1,len(nums)):
            ans.append(nums[idx] + ans[-1])
        return ans