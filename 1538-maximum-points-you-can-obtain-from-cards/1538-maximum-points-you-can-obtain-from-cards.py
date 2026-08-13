class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = sum(cardPoints)
        total = sum(cardPoints)
        if k == len(cardPoints):
            return max_sum

        state = 0
        max_points = 0
        start = 0

        for end in range(len(cardPoints)):
            state += cardPoints[end]
            if end - start + 1 == len(cardPoints) - k: #for difference of the remaining cards
                max_points = max(max_sum - state, max_points)
                state -= cardPoints[start]
                start += 1
        return max_points