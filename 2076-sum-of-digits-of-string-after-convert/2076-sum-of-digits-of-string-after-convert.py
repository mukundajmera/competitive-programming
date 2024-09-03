class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = [ord(ch) - ord('a') +1  for ch in s]

        while k > 0:
            k -= 1
            temp_dir = []
            value = 0
            for num in result:
                count = 0
                while num > 0:
                    digit = num % 10
                    num = num // 10
                    count += digit
                value += count
            temp_dir.append(value)
            result = temp_dir
        return result[0]