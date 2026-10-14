class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def dfs(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[index])
            dfs(index+1, path)

            #exclude number
            path.pop()
            dfs(index+1, path)    
        
        dfs(0, [])
        return result