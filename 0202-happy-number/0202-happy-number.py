class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum([int(idx) ** 2 for idx in str(n)])
        return n == 1
        # num_square = {i:i**2 for i in range(0,11)}
        # # print(num_square)
        # is_happy = False
        # numbers = n
        # execution = 1000
        # while execution > 0 :
        #     current_sum = 0
        #     while numbers > 0:
        #         digit = numbers % 10
        #         numbers //= 10
        #         # print(type(digit), digit, num_square.get(digit))
        #         current_sum += num_square.get(digit)
        #     if current_sum == 1:
        #         return True
        #     numbers = current_sum
        #     execution -= 1
        # return False