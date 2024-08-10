directions = [(-1,0), (1,0), (0,1), (0,-1)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        count = 0
        for r in range(0, nr):
            for c in range(0, nc):
                if grid[r][c] == '1':
                    count += 1
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
                        if row + 1 < nr and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"
                        if col + 1 < nc and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
                # queue = Deque([(row,col)])
                # while queue:
                #     row, col = queue.popleft()
                #     grid[row][col] = 0
                #     for nr, nc in directions:
                #         nr += row
                #         nc += col
                #         if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == '1':
                #             queue.append((nr,nc))
        return count