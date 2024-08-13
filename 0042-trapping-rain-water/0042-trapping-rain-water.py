class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        idx = 0
        stack = []
        while idx < len(height):
            
            while len(stack) != 0 and height[idx] > height[stack[-1]]:
                peak = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                distance = idx - stack[-1] -1
                water_height = min(height[idx], height[stack[-1]]) - height[peak]
                water += distance * water_height
                
            stack.append(idx)
            idx += 1
        return water
    # def trap(self, height: List[int]) -> int:
    #     #edge case
    #     if len(height) == 0:
    #         return 0
    #     water = 0
    #     left ,right = 0, len(height)-1
    #     left_max, right_max = 0 , 0
    #     while left < right:
    #         if height[left] > left_max:
    #             left_max = height[left]
    #         if height[right] > right_max:
    #             right_max = height[right]
            
    #         #move the lower one for opposite max seen
    #         if left_max > right_max:
    #             water += max(0, right_max - height[right])
    #             right -= 1
    #         else:
    #             water += max(0, left_max - height[left])
    #             left += 1
    #     return water
            
