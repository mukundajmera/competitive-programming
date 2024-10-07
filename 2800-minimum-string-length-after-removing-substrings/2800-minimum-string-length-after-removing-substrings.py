class Solution:
    # def remove_substring(self, string: str, pattern):
    #     index = string.find(pattern)
    #     # print(string, index, len(string))
    #     string = string[:index] + string[index+2:]
    #     return string
        
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            
            if ch == "B" and stack[-1] == "A":
                stack.pop()
            elif ch == "D" and stack[-1] == "C":
                stack.pop()            
            else:
                stack.append(ch)

        return len(stack)
        # while "AB" in s or "CD" in s:
        #     if "AB" in s:
        #         s = self.remove_substring(s, "AB")
        #     if "CD" in s:
        #         s = self.remove_substring(s, "CD")
        
        # return len(s)
