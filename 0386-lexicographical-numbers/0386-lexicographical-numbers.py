class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        numbers = []
        for idx in range(1, 10):
            self._lexical_numbers(idx, n, numbers)
        return numbers
    
    def _lexical_numbers(self, current, limit, result):
        if current > limit:
            return
        
        result.append(current)
        for next_digit in range(10):
            next_number = current * 10 + next_digit
            if next_number <= limit:
                self._lexical_numbers(next_number, limit, result)
            else:
                break
