class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = 0
        current_sum = 0

        for idx in range(len(grid)-2):
            for idj in range(1, len(grid[0])-1):
                current_sum = sum(grid[idx][idj - 1: idj+2]) + grid[idx+1][idj] + sum(grid[idx+2][idj-1:idj+2])
                result = max(result, current_sum)
        
        return result
