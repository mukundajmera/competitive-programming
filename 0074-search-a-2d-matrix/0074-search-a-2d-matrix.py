class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.binary_search(row, target)
        
        return False
        