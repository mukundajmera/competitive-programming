class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+" : lambda a,b : a+b,
            "-" : lambda a,b : a-b,
            "/" : lambda a,b : int(a/b),
            "*" : lambda a,b : a*b,
        }
        #using stack appraoch for operations
        stack = []
        for op in tokens:
            if op in operations:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operations[op](op1,op2))
            else:
                stack.append(int(op))
        return stack[-1]
