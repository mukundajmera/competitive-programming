class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        nrow, ncol = len(grid1), len(grid1[0])
        visited = set()
        count = 0
        def dfs(r,c):
            if r < 0 or r == nrow or c < 0 or c == ncol or grid2[r][c] == 0 or (r,c) in visited:
                return True
            visited.add((r,c))
            result = True
            if grid1[r][c] == 0:
                result = False
            result = dfs(r - 1, c) and result
            result = dfs(r + 1,c) and result
            result = dfs(r ,c + 1) and result
            result = dfs(r ,c - 1) and result
            return result
        
        for r in range(nrow):
            for c in range(ncol):
                if grid2[r][c] ==  1 and (r,c) not in visited and dfs(r,c):
                    # print((r,c))
                    count += 1
        return count