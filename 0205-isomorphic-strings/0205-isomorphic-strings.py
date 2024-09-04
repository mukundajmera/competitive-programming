class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapA = {}
        mapB = {}
        if len(s) != len(t):
            return False
        for ch1, ch2 in zip(s,t):
            if (ch1 not in mapA) and (ch2 not in mapB):
                mapA[ch1] = ch2
                mapB[ch2] = ch1
            elif mapA.get(ch1) != ch2 or mapB.get(ch2) != ch1:
                return False
        return True