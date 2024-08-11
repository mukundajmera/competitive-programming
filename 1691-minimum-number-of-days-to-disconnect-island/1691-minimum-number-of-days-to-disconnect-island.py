class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def _count_islands():
            visited = set()
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        _explore_island(i, j, visited)
                        count += 1
            return count

        def _explore_island(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                _explore_island(i + di, j + dj, visited)

        # Check if already disconnected
        if _count_islands() != 1:
            return 0

        # Check if can be disconnected in 1 day
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if _count_islands() != 1:
                        return 1
                    #unset the count for checking all the islands important
                    grid[i][j] = 1

        # If can't be disconnected in 0 or 1 day, return 2
        return 2

        # count = 0
        # queue = Deque()
        # count_one = 0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             count += 1
        #             #do something
        #             queue = Deque([(r,c,)])
        #             while queue:
        #                 r,c = queue.popleft()
        #                 grid[r][c] = 0
        #                 count_one += 1
        #                 for nr,nc in [(0,1), (0,-1), (1,0), (-1,0)]:
        #                     nr += r
        #                     nc += c
        #                     if 0<= nr < len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc] == 1:
        #                         queue.append((nr,nc))
        # # print(count)
        # if count == 0:
        #     return count
        # if count == 1 and count_one == 1:
        #     return 1
        # return 2