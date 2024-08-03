class Solution:
    def reverseBits(self, n: int) -> int:
        length = 31
        number = 0
        while n:
            #add right most bit
            number += (n & 1) << length
            # remove it
            n = n >> 1
            #decrease the power
            length -= 1
        return number