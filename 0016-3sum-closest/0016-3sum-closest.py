import heapq
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = []
        nums.sort()
        for idx in range(len(nums)-2):
            left = idx + 1
            right = len(nums)-1
            while left < right:
                temp = nums[idx] + nums[left] + nums[right]
                heapq.heappush(closest,(abs(target - temp),temp))
                if temp < target:
                    left += 1
                else:
                    right -=1

        return heapq.heappop(closest)[1]
