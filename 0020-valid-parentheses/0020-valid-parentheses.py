class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")" : "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in mapping:
                if len(stack) == 0 or mapping[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0