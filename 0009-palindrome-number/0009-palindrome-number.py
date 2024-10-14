class Solution:
    def isPalindrome(self, x: int) -> bool:
        #use unit calcuation on digit
        number = x
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number //= 10
        return reverse == x
        # return str(x)[::] == str(x)[::-1]