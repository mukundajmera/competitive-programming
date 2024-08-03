class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def generateString(word):
            string = ''
            for ch in word:
                if ch != '#':
                    string += ch
                else:
                    string = string[:-1]
            return string
        return generateString(s) == generateString(t)        
        # #using stack approach
        # stack1, stack2 = [], []
        # for ch in s:
        #     if ch == "#":
        #         if not stack1:
        #             continue
        #         stack1.pop()
        #     else:
        #         stack1.append(ch)

        # for ch in t:
        #     if ch == "#":
        #         if not stack2:
        #             continue
        #         stack2.pop()
        #     else:
        #         stack2.append(ch)
        # return stack1 == stack2