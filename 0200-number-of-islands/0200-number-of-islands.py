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

        # nr = len(grid)
        # nc = len(grid[0])
        # count = 0
        # for r in range(0, nr):
        #     for c in range(0, nc):
        #         if grid[r][c] == '1':
        #             count += 1
        #             neighbors = []
        #             neighbors.append((r, c))
        #             while neighbors:
        #                 row, col = neighbors.pop(0)
        #                 if row - 1 >= 0 and grid[row - 1][col] == "1":
        #                     neighbors.append((row - 1, col))
        #                     grid[row - 1][col] = "0"
        #                 if row + 1 < nr and grid[row + 1][col] == "1":
        #                     neighbors.append((row + 1, col))
        #                     grid[row + 1][col] = "0"
        #                 if col - 1 >= 0 and grid[row][col - 1] == "1":
        #                     neighbors.append((row, col - 1))
        #                     grid[row][col - 1] = "0"
        #                 if col + 1 < nc and grid[row][col + 1] == "1":
        #                     neighbors.append((row, col + 1))
        #                     grid[row][col + 1] = "0"
        #         # queue = Deque([(row,col)])
        #         # while queue:
        #         #     row, col = queue.popleft()
        #         #     grid[row][col] = 0
        #         #     for nr, nc in directions:
        #         #         nr += row
        #         #         nc += col
        #         #         if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == '1':
        #         #             queue.append((nr,nc))
        # return count