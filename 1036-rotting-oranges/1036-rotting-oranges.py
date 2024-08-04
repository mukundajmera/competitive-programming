class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minute = -1
        rot = deque()
        has_orange = False            # whether grid contain an orange
        for x in range(m):
            for y in range(n):
                has_orange = has_orange or grid[x][y]
                if grid[x][y] == 2:   # rotten orange
                    rot.append((x, y))
        if not has_orange: return 0   # no orange in grid, return 0
        while rot:          # bfs to rot oranges
            minute += 1
            count = len(rot)
            for _ in range(count):
                x, y = rot.popleft()
                if x+1 < m and grid[x+1][y] == 1:
                        grid[x+1][y] = 2
                        rot.append((x+1, y))
                if x-1 >= 0 and grid[x-1][y] == 1:
                        grid[x-1][y] = 2
                        rot.append((x-1, y))
                if y+1 < n and grid[x][y+1] == 1:
                        grid[x][y+1] = 2
                        rot.append((x, y+1))
                if y-1 >= 0 and grid[x][y-1] == 1:
                        grid[x][y-1] = 2
                        rot.append((x, y-1))
        for x in range(m):    # check for unrotten oranges
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
        return minute