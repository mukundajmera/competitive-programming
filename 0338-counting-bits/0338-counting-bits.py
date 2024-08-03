class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        if n == 0:
            return result
        result[0] = 0
        if n >= 1:
            result[1] = 1
        for x in range(2, n + 1):
            if x % 2 == 0:
                result[x] = result[x // 2]
            else:
                result[x] = result[x // 2] + 1
            # print(x, result)
        return result
        

        # answer = [0] * (n + 1)
        # for num in range(1, n+1):
        #     answer[num] = answer[num & (num-1)] + 1
        # return answer