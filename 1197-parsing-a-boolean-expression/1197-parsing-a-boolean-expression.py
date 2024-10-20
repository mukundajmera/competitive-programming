class Solution:
    def _eval_exp(self, op, values):
        if op == "!":
            return "f" if values[0] == "t" else "t"

        if op == "&":
            for value in values:
                if value == "f":
                    return "f"
            return "t"

        if op == "|":
            for value in values:
                if value == "t":
                    return "t"
            return "f"

        return "f"

    def parseBoolExpr(self, expression: str) -> bool:
        #using stack
        st = deque()

        for curr_char in expression:
            if curr_char == ")":
                values = []
                
                while st[-1] != "(":
                    values.append(st.pop())
                st.pop() #opening braces
                op = st.pop()
                result = self._eval_exp(op, values)
                st.append(result)
            elif curr_char != ",":
                st.append(curr_char)

        return st[-1] == "t"