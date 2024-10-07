class Solution:
    def remove_substring(self, string: str, pattern):
        index = string.find(pattern)
        # print(string, index, len(string))
        string = string[:index] + string[index+2:]
        return string
        
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = self.remove_substring(s, "AB")
            if "CD" in s:
                s = self.remove_substring(s, "CD")
        
        return len(s)
