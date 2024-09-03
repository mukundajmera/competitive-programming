class Solution:
    def romanToInt(self, s: str) -> int:
        rval = {"I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
        idx = len(s)-1
        value = 0
        #read in reverse order
        while idx >= 0:
            curr_val = rval.get(s[idx])
            negative = 0
            while idx-1 >= 0 and rval.get(s[idx - 1]) < curr_val:
                idx -= 1
                negative += rval.get(s[idx])
            value += (curr_val - negative)
            # print(idx, curr_val, negative, value)
            idx -= 1
        return value