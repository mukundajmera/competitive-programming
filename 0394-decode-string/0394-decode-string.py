class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == "]":
                #pop to make string will to find
                partial_pattern = ""
                while stack[-1] != "[":
                    partial_pattern += stack.pop()

                partial_pattern = partial_pattern[::-1]
                stack.pop()
                #get digit
                digit = []
                # print(digit, stack)
                while len(stack) > 0 and stack[-1] in "1234567890":
                    digit.append(stack.pop())
                # print(digit, stack, partial_pattern)
                partial_pattern *= int("".join(digit[::-1]))
                stack.extend(partial_pattern)
                
            else:
                stack.append(s[idx])
            idx += 1
        return "".join(stack)
                
            