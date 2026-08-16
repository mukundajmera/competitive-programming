class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        max_len = 0
        start = 0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1

            while state[s[end]] > 1:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1

            max_len = max(max_len, len(state))

        return max_len