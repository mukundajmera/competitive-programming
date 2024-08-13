class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        candidates.sort()
        def dfs(index, stack, target):
            if target == 0:
                combination.append(stack.copy())
                return
            if target < 0:
                return
            for idx in range(index, len(candidates)):
                current_sum = sum(stack)
                if idx > index and candidates[idx] == candidates[idx-1]:
                    continue;
                stack.append(candidates[idx])
                # print(idx , stack, target - candidates[idx])
                dfs(idx+1, stack, target - candidates[idx])
                stack.pop()
        
        dfs(0, [], target)
        return list(combination)