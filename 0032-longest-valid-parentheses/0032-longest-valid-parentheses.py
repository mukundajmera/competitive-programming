class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]

        for idx, ch  in enumerate(s):
            if ch == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                max_len = max(max_len, idx - stack[-1])
            #print(idx, stack, max_len)
        return max_len