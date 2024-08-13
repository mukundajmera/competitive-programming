class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort(reverse=True)
        def dfs(target, stack, index):
            if target < 0:
                return
            if target == 0:
                result.append(stack.copy())
            
            for idx in range(index, len(candidates)):
                stack.append(candidates[idx])
                dfs(target- candidates[idx], stack, idx)
                stack.pop()
        
        dfs(target, [], 0)
        return result
