class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            if s[end] in state:
                start = max(start, state[s[end]] + 1)
            state[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length

        # state = {}
        # max_len = 0
        # start = 0
        # for end in range(len(s)):
        #     state[s[end]] = state.get(s[end], 0) + 1

        #     while state[s[end]] > 1:
        #         state[s[start]] -= 1
        #         if state[s[start]] == 0:
        #             del state[s[start]]
        #         start += 1

        #     max_len = max(max_len, len(state))

        # return max_len