class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for idx in range(len(strs[0])):
            char = strs[0][idx]
            for other in range(1, len(strs)):
                if idx == len(strs[other]) or char != strs[other][idx]:
                    return strs[0][:idx]
        return strs[0]
        # if strs == None or len(strs) == 0:
        #     return ""
        # for idx in range(len(strs[0])):
        #     char = strs[0][idx]
        #     for other_word in range(1, len(strs)):
        #         if idx == len(strs[other_word]) or char != strs[other_word][idx]:
        #             return strs[0][0:idx]
        # return strs[0]