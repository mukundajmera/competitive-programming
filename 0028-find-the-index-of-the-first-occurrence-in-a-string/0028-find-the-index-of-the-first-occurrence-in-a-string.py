class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #sliding window of fixed size
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx + len(needle)] == needle:
                return idx
        return -1
        # result = -1
        # idx = 0
        # if len(needle) > len(haystack):
        #     return -1
        # for ch in range(len(haystack)):
        #     if haystack[ch] == needle[0] and len(needle) <= len(haystack) - ch:
        #         substr = True
        #         for val in range(len(needle)):
        #             if (ch + val < len(haystack) and needle[val] != haystack[ch + val]) or ch + val > len(haystack):
        #                 substr = False
        #                 break
        #         if substr:
        #             result = ch
        #             break
        # return result
            