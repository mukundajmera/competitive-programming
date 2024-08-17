class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #using hash map
        sub_map = {}
        sub_map[0] = 1
        sum  = 0
        count = 0
        for idx in range(len(nums)):
            sum += nums[idx]
            if (sum - k) in  sub_map:
                # print("i am in")
                count += sub_map[sum-k]
            sub_map[sum] = sub_map.get(sum,0) + 1
            # print(sub_map, sum-k)
        return count
        # prefix_sum = [0] * (len(nums) + 1)
        # count = 0
        # for idx in range(1, len(prefix_sum)):
        #     prefix_sum[idx] = prefix_sum[idx-1] + nums[idx-1]

        # # print(prefix_sum)

        # for idx in range(len(nums)+1):
        #     for end in range(idx+1, len(nums)+1):
        #         if(prefix_sum[end] - prefix_sum[idx] == k):
        #             count += 1

        # return count    
