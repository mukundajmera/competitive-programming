class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        def get_neighbours(x, y):
            neighbours = []
            for dx, dy in dirs:
                if 0 <= x+dx < n and 0 <= y+dy < n:
                    neighbours.append((x+dx, y+dy))
            return neighbours
        length = 1
        q = deque()
        q.append((0,0))
        unvisited = [[True for _ in range(n)] for _ in range(n)]
        unvisited[0][0] = False
        while q:
            count = len(q)
            for _ in range(count):
                x, y = q.popleft()
                if x == n -1 and y == n-1:
                    return length
                for nx, ny in get_neighbours(x, y):
                    if grid[nx][ny] == 0 and unvisited[nx][ny]:
                        q.append((nx, ny))
                        unvisited[nx][ny] = False
            length += 1
        return -1