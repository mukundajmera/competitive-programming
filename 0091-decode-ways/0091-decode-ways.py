class Solution:
    def numDecodings(self, digits: str) -> int:
        memo = {}
        def dfs(index, memo):
            if index in memo:
                return memo[index]
            if index == len(digits):
                return 1
            answer = 0
            ways = 0
            # can't decode string with leading 0
            if digits[index] == '0':
                return answer
            
            # decode one digit
            answer += dfs(index + 1, memo)
            
            # decode two digits
            if 10 <= int(digits[index: index + 2]) <= 26:
                answer += dfs(index + 2, memo)
            memo[index] = answer
            return answer        
        return dfs(0, memo)
