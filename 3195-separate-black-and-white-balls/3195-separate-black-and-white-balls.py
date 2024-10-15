class Solution:
    def minimumSteps(self, s: str) -> int:
        left, right = 0, len(s)-1
        while left < len(s):
            if s[left] != '0':
                break
            left += 1

        while right >= 0:
            if s[right] != '1':
                break
            right -= 1
        
        count = 0
        while left < right:
            if s[left] == '1' and s[right] == '0':
                count += right - left
                left += 1
                right -= 1
                continue
            
            while left < len(s) and s[left] == '0':
                left += 1
            
            while right >= 0 and s[right] == '1':
                right -= 1
        
        return count

            