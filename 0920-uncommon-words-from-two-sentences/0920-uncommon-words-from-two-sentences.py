class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = defaultdict(int)
        for word in s1.split(" "):
            words[word] += 1

        for word in s2.split(" "):
            words[word] += 1
            
        uncommon = []
        for key, value in words.items():
            if value == 1:
                uncommon.append(key)
        return uncommon