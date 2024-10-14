class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #base case
        if left == right:
            return left

        shift_count = 0
        while left != right:
            left = left >> 1
            right = right >> 1

            shift_count += 1
        

        return left << shift_count