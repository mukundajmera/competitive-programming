class Solution:
    def minimumDeletions(self, s: str) -> int:
        length = len(s)
        countA = [0]*length
        countB = [0]*length

        cb, ca = 0,0
        for idx in range(length):
            countB[idx] = cb
            if s[idx] == "b":
                cb += 1

        for idx in reversed(range(length)):
            countA[idx] = ca
            if s[idx] == "a":
                ca += 1
        #max by default
        min_del = length
        for idx in range(length):
            min_del = min(min_del, countA[idx] + countB[idx])
        
        return min_del
