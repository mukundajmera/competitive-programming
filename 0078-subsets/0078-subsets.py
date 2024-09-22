class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        #using dfs approach
        def dfs(index, stack):
            if index == len(nums):
                result.append(stack.copy())
                return
            stack.append(nums[index])
            dfs(index+1, stack)
            stack.pop()
            dfs(index+1, stack)
        
        dfs(0, [])
        return list(result)
