class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if not chalk:
            return 0
        k = k % sum(chalk)
        if k == 0:
            return 0        
        for idx in range(len(chalk)):
            if chalk[idx] <= k:
                k -= chalk[idx]
            else:
                return idx
        return k