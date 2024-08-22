class Solution:
    def findComplement(self, num: int) -> int:
        # print(1 << num.bit_length())
        value = num ^ ((1 << num.bit_length()) -1)
        return value
