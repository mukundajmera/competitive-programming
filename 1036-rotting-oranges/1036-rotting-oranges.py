class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        nrows, ncols = len(grid), len(grid[0])
        queue = deque()
        fresh_orange = 0

        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_orange += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh_orange > 0:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for nr, nc in directions:
                    nr += row
                    nc += col
                    if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_orange -= 1
                        queue.append((nr,nc))

        return minutes if fresh_orange == 0 else -1