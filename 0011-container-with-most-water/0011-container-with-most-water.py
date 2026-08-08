class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height)-1

        max_area = 0
        while left < right:
            width = right - left
            current_heigh = min(height[left], height[right])

            max_area = max(max_area, current_heigh * width)

            #iteration
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area