class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        mapA = {}
        mapB = {}
        if len(pattern) != len(words):
            return False
        for ch1, word in zip(pattern, words):
            if ch1 not in mapA and word not in mapB:
                mapA[ch1] = word
                mapB[word] = ch1
            elif mapA.get(ch1) != word or mapB.get(word) != ch1:
                return False
        return True