class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[::] = digits[::-1]
        digits[0] += 1
        carry = 0
        for idx in range(len(digits)):
            digits[idx] += carry
            carry = 0
            if digits[idx] < 10:
                break
            else:
                digits[idx] %= 10
                carry = 1
        if carry == 1:
            digits.append(carry)

        return digits[::-1]
            

