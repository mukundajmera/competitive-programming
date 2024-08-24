class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for number in nums:
            digits = 0
            while number > 0:
                number //= 10
                digits += 1
            if digits % 2 == 0:
                count += 1
        return count
    