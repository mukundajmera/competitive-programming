class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        possible = True
        word_map = {}
        for ch in magazine:
            word_map[ch] = word_map.get(ch,0) + 1
        #magazine check
        for ch in ransomNote:
            if ch in word_map:
                word_map[ch] -= 1
                if word_map[ch] == 0:
                    del word_map[ch]
            else:
                possible = False
                break        
        return possible

    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ct1, ct2 = Counter(ransomNote), Counter(magazine)        
        # return True if ct1 & ct2 == ct1 else False

