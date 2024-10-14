class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        alen, blen = len(a), len(b)

        while alen > 0 or blen > 0 or carry:
            if alen > 0:
                carry += int(a[alen-1])
                alen -= 1
            
            if blen > 0:
                carry += int(b[blen-1])
                blen -= 1
            
            s.append(str(carry % 2))
            carry //= 2
        
        return "".join(reversed(s))