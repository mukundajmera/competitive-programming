class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Your code goes here
        nums.sort()

        pairs = 0
        for idx in range(len(nums)- 1, 1, -1):
            left = 0
            right = idx - 1
            while left < right:
                if nums[left] + nums[right] > nums[idx]:
                    pairs += right - left
                    right -= 1
                else:
                    left += 1
        return pairs