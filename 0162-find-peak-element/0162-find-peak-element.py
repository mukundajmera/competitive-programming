class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        index = 0
        if len(nums) < 2:
            return 0
        while left <= right:
            mid = (left + right)//2
            if mid+1 < len(nums) and nums[mid] < nums[mid+1]:                
                left = mid + 1
            else:
                right = mid - 1
        # print(peak, left, right)
        return left
