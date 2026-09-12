class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            count = self.countLessOrEqual(matrix, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
    
    def countLessOrEqual(self, matrix, mid):
        n = len(matrix)
        count = 0
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            #print(f"{row=} {col=} {count=}")
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        #print(count, mid)
        return count