class Solution:
    def findComplement(self, num: int) -> int:
        value = num ^ ((1 << num.bit_length()) -1)
        return value
