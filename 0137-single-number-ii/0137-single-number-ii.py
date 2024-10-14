class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = sum(set(nums))
        result = ((3 * unique) - sum(nums)) // 2
        return result
        # ones = 0
        # twos = 0

        # for num in nums:
        #     ones ^= (num & ~twos)
        #     twos ^= (num & ~ones)

        # return ones