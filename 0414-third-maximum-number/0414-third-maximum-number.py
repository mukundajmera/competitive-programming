class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one,two,three= -inf, -inf, -inf

        for num in nums:
            if one == num or two == num or three == num:
                continue
            
            if one <= num:
                three = two
                two = one
                one = num
            elif two <= num:
                three = two
                two = num
            elif three <= num:
                three = num

        if three == -inf:
            return one
        return three

                