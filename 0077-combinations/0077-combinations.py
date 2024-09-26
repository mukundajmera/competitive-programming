class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        def dfs(index, stack):
            if len(stack) == k:
                combination.append(stack[:])
                return

            for idx in range(index, n+1):
                if len(stack) < k:
                    stack.append(idx)
                    dfs(idx + 1, stack)
                    stack.pop()
        
        dfs(1, [])
        return combination
