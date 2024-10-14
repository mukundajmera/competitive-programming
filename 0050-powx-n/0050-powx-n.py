class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        #base case
        if n < 0:
            flag = -1
        else:
            flag =  1
        
        n = abs(n)
        while n != 0:
            if n % 2 == 0:
                x = x * x
                n //= 2
            else:
                answer = answer * x
                n -= 1
        
        if flag == -1:
            return 1 / answer
        return answer
                
