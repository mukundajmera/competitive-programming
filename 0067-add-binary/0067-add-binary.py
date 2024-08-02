class Solution:
    def addBinary(self, a, b) -> str:
        answer = []
        carry = 0
        ida, idb = len(a)-1, len(b)-1
        while ida >= 0 or idb >= 0 or carry:
            if ida >= 0:
                carry += int(a[ida])
                ida -= 1
            if idb >= 0:
                carry += int(b[idb])
                idb -= 1
            answer.append(str(carry % 2))
            carry //= 2
        return "".join(answer[::-1])
            

    # def addBinary(self, a, b) -> str:
    #     n = max(len(a), len(b))
    #     a, b = a.zfill(n), b.zfill(n)
        
    #     answer = []
    #     count = 0
    #     for idx in reversed(range(n)):
    #         if a[idx] == "1":
    #             count += 1
    #         if b[idx] == "1":
    #             count += 1
    #         if count % 2 == 1:
    #             answer.append('1')
    #         else:
    #             answer.append('0')
    #         count = count // 2
    #     if count == 1:
    #         answer.append('1')
    #     return "".join(answer[::-1])


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