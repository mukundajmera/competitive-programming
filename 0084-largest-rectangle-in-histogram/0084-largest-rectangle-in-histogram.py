class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        idx = 0
        max_area = 0

        while idx < len(heights):
            if not stack or heights[idx] >= heights[stack[-1]]:
                stack.append(idx)
                idx += 1                
            else:
                value = stack.pop()
                right = idx - 1
                left = stack[-1] if stack else -1
                area = heights[value] * (right - left)
                max_area = max(max_area, area)
        while stack:
            value = stack.pop()
            width = idx - stack[-1] - 1 if stack else idx
            area = heights[value] * width
            max_area = max(max_area, area)
        return max_area