class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(stack):
            if len(nums) == len(stack):
                result.append(stack.copy())
            
            for idx in range(len(nums)):
                if nums[idx] not in stack:
                    stack.append(nums[idx])
                    dfs(stack)
                    stack.pop()
        
        dfs([])
        return result
