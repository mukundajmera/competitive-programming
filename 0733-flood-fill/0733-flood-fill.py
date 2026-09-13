class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nrow, ncol = len(image), len(image[0])

        original = image[sr][sc]
        if original == color:
            return image
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row, col):
            if image[row][col] == original:
                image[row][col] = color
            else:
                return
            
            for r,c in direction:
                next_row = row + r
                next_col = col + c
                if next_row < 0 or next_row >= nrow or next_col < 0 or next_col >= ncol:
                    continue
                dfs(next_row, next_col)
            return
        
        dfs(sr, sc)
        return image

        # directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # nrow, ncol = len(image), len(image[0])
        # #using BFS approach
        # queue = deque()
        # queue.append((sr,sc))
        # current_color = image[sr][sc]
        # seen = set()
        # while queue:
        #     pixel = queue.popleft()
        #     row, col = pixel[0], pixel[1]
        #     image[row][col] = color
        #     seen.add((row, col))
        #     for new_row, new_col in directions:
        #         new_row += row
        #         new_col += col
        #         if 0 <= new_row < nrow and 0 <= new_col < ncol and image[new_row][new_col] == current_color and (new_row, new_col) not in seen:
        #             queue.append((new_row, new_col))
        # return image