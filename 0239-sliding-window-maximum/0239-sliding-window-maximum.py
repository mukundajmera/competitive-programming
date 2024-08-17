class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = Deque()
        for idx, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)

            if idx >= k and nums[idx - k] == queue[0]:
                queue.popleft()
            
            if idx >= k - 1:
                result.append(queue[0])
        return result

        # max_values = []
        # for idx in range(len(nums)-k+1):
        #     max_values.append(max(nums[idx : idx + k]))
        # return max_values