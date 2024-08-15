class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        is_possible = True
        if bills[0] != 5:
            return False
        doller_5 = 0
        doller_10 = 0
        for bill in bills:
            if bill == 5:
                doller_5 += 1
            elif bill == 10:
                if doller_5 > 0:
                    doller_5 -= 1
                else:
                    is_possible = False
                    break
                doller_10 += 1
            else:
                if doller_5 > 0 and doller_10 > 0:
                    doller_5 -= 1
                    doller_10 -= 1
                elif doller_5 > 2:
                    doller_5 -= 3
                else:
                    is_possible = False
                    break                    
        return is_possible