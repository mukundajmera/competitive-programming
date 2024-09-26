class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combination = []
        def dfs(index, stack):
            if index == len(nums):
                combination.append(stack[:])
                return

            for idx in range(0, len(nums)):
                if nums[idx] not in stack:
                    stack.append(nums[idx])
                    dfs(index + 1, stack)
                    stack.pop()
        
        dfs(0, [])
        return combination
