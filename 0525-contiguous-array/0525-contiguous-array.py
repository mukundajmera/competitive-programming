class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_0, count_1 = 0, 0
        number_map = {}
        number_map[0] = -1
        answer = 0

        for idx in range(len(nums)):
            if(nums[idx] == 0):
                count_0 += 1
            else:
                count_1 += 1
            
            if(number_map.get(count_1 - count_0) == None):
                number_map[count_1 - count_0] = idx
            else:
                answer = max(answer, idx - number_map[count_1 - count_0])
            # print(idx, number_map,count_0, count_1, nums, answer)
        return answer
