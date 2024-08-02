class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        word_count = Counter(s)
        for key, value in word_count.items():
            if value % 2 != 0:
                odd_count += 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        else:
            return len(s)

    # def longestPalindrome(self, s: str) -> int:
    #     odd_count = 0
    #     freq = {}
    #     for ch in s:
    #         freq[ch] = freq.get(ch, 0) + 1
    #         if freq.get(ch) % 2 == 0:
    #             odd_count -= 1
    #         else:
    #             odd_count += 1
    #     print(odd_count)
    #     if odd_count > 0:
    #         return len(s) - odd_count + 1
    #     else:
    #         return len(s)