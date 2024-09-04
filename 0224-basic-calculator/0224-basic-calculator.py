class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign = 1
        result = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                #shift current digit
                number = number * 10 + int(ch)
            elif ch in "+-":
                result += number * sign
                if ch == "-":
                    sign = -1
                else:
                    sign = 1
                #reset it
                number = 0
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                #reset it
                result = 0
                sign = 1
            elif ch == ")":
                result += sign * number
                result *= stack.pop()
                result += stack.pop()
                #reset it
                number = 0
        #covering last case
        return result + number * sign