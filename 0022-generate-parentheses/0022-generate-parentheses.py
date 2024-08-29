class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        combination = []

        def dfs(open_number, close_number):
            #close case
            if open_number == close_number == n:
                combination.append("".join(stack))
                return
            
            if open_number < n:
                stack.append("(")
                dfs(open_number + 1, close_number)
                stack.pop()
            if close_number < open_number:
                stack.append(")")
                dfs(open_number, close_number + 1)
                stack.pop()            
        
        dfs(0, 0)
        return combination