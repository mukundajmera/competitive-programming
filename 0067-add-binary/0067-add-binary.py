class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        answer = []
        count = 0
        for idx in reversed(range(n)):
            if a[idx] == "1":
                count += 1
            if b[idx] == "1":
                count += 1
            if count % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            count = count // 2
        if count == 1:
            answer.append('1')
        return "".join(answer[::-1])


    # def addBinary(self, a, b) -> str:
    #     n = max(len(a), len(b))
    #     a, b = a.zfill(n), b.zfill(n)

    #     carry = 0
    #     answer = []
    #     for i in range(n - 1, -1, -1):
    #         if a[i] == "1":
    #             carry += 1
    #         if b[i] == "1":
    #             carry += 1

    #         if carry % 2 == 1:
    #             answer.append("1")
    #         else:
    #             answer.append("0")

    #         carry //= 2

    #     if carry == 1:
    #         answer.append("1")
    #     answer.reverse()

    #     return "".join(answer)