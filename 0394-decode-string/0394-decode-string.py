class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        current_number = 0

        for ch in s:
            if ch.isdigit():
                current_number = int(ch) + 10 * current_number
            elif ch == "[":
                stack.append(curr_string)
                stack.append(current_number)
                curr_string = ""
                current_number = 0
            elif ch == "]":
                prev_num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + prev_num * curr_string
            else:
                curr_string += ch
            #print(stack, curr_string, current_number)
        return curr_string 