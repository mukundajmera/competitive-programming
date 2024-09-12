class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        # if len(houses) < 3:
        #     return max(houses)
        # max_till_now = [0] * len(houses)
        # max_till_now[0], max_till_now[1] = houses[0], houses[1]

        # for house_idx in range(2, len(houses)):
        #     if house_idx - 3 > 0:
        #         max_till_now[house_idx] = max(max_till_now[house_idx - 2] + houses[house_idx],
        #                                     max_till_now[house_idx - 3] + houses[house_idx])
        #     else:
        #         max_till_now[house_idx] = max_till_now[house_idx - 2] + houses[house_idx]

        # return max(max_till_now[-1], max_till_now[-2])
