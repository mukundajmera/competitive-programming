class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        nrow, ncol = len(matrix), len(matrix[0])
        left, right = 0, ncol - 1
        up, down = 0, nrow - 1

        while len(result) < nrow * ncol:
            #right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            #down
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            if up == down:
                break

            #left
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[down][col])

            if left == right:
                break

            #up
            for row in range(down - 1, up, -1):
                result.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
