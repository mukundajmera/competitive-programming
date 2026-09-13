class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nrow , ncol = len(grid), len(grid[0])
        direction = [(0,1),(-1,0),(1,0),(0,-1)]
        count = 0
        def dfs(r, c):
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr,dc in direction:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < nrow and 0 <= nc < ncol:
                    dfs(nr, nc)
            return

        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row,col)
        
        return count