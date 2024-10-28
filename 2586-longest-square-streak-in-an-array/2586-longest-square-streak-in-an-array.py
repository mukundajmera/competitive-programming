class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest = 0
        numbers = set(nums)

        for num in nums:
            current = 0
            current_num = num
            while current_num in numbers:
                current += 1
                if current ** 2 > 10 ** 5:
                    break
                current_num *= current_num
            
            longest = max(longest, current)
        
        return longest if longest > 1 else -1