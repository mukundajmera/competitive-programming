import string
class Solution:
    def minimumPushes(self, word: str) -> int:
        char_map = [0] * 26
        for ch in word:
            char_map[ord(ch) - ord('a')] += 1
        char_map.sort(reverse=True)
        # print(char_map)
        count = 0
        #total count
        for idx in range(26):
            if char_map[idx] == 0:
                continue
            count += ((idx // 8) + 1) * char_map[idx]
            # print(idx, count)
        return count