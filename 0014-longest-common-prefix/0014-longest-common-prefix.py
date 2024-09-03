class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #base case
        if strs == None or len(strs) == 0:
            return ""
        for ch in range(len(strs[0])):
            #compare first string with rest
            char = strs[0][ch]
            for str2 in range(1, len(strs)):
                if ch == len(strs[str2]) or char != strs[str2][ch]:
                    return strs[0][:ch]
        return strs[0]
        # if strs == None or len(strs) == 0:
        #     return ""
        # for idx in range(len(strs[0])):
        #     char = strs[0][idx]
        #     for other_word in range(1, len(strs)):
        #         if idx == len(strs[other_word]) or char != strs[other_word][idx]:
        #             return strs[0][0:idx]
        # return strs[0]