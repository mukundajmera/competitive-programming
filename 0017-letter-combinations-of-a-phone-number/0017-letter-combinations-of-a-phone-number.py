class Solution:
    digits_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz", 
    }
    def letterCombinations(self, digits: str) -> List[str]:
        combination = []

        if not digits:
            return []

        def dfs(index, stack):
            if index == len(digits):
                combination.append("".join(stack))
                return

            for digit in self.digits_map.get(digits[index]):
                stack.append(digit)
                dfs(index + 1, stack)
                stack.pop()
                
        dfs(0, [])
        return combination