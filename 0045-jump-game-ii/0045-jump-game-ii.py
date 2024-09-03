class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            far = 0
            for idx in range(left, right + 1):
                far = max(far, idx + nums[idx])
            left = right + 1
            right = far
            count += 1

        return count
        
        return count
