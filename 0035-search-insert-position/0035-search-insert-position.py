class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) -1
        index = 0
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1                
            else:
                left = mid + 1                
        return left
