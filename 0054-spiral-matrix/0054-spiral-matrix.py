class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, cols = len(matrix), len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1

        while len(result) < rows * cols:
            # travers to right
            for col in range(left, right+1):
                result.append(matrix[up][col])

            # traverse to down
            for row in range(up+1, down+1):
                result.append(matrix[row][right])
                
            if up == down:
                break

            # traverse to left
            for col in range(right -1, left-1, -1):
                result.append(matrix[down][col])

            if left == right:
                break

            # traverse to up
            for row in range(down - 1, up, -1):
                result.append(matrix[row][left])
                
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result