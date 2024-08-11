class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(target, stack, start):
            if target == 0:
                result.append(list(stack))
                return
            elif target < 0:
                return
            
            for idx in range(start, len(candidates)):
                stack.append(candidates[idx])
                dfs(target - candidates[idx], stack, idx)
                stack.pop()
        
        dfs(target, [], 0)
        return result
