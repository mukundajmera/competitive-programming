class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counterT, counterArr = Counter(target), Counter(arr)
        return counterT == counterArr