class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temprature = [0] * len(temperatures)
        for idx, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                    index, _ = stack.pop()
                    temprature[index] = idx - index
            stack.append((idx, value))
        return temprature