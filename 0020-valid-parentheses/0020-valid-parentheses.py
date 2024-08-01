class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(":")", "{":"}","[":"]"}
        stack = []
        for idx in range(len(s)):
            if s[idx] in braces:
                stack.append(s[idx])
            elif s[idx] in braces.values():
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if s[idx] != braces[opening]:
                    return False
        if len(stack) > 0:
            return False
        return True