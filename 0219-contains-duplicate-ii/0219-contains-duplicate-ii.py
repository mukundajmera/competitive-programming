class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        common_set = set()
        for idx in range(len(nums)):
            # print(nums[idx], common_set)
            if nums[idx] in common_set:
                return True
            common_set.add(nums[idx])
            if len(common_set) > k:
                common_set.remove(nums[idx-k])
        return False
#         counter = {}
#         for idx in range(len(nums)):
#             if nums[idx] in counter:
#                 counter[nums[idx]].append(idx)
#             else:
#                 counter[nums[idx]] = [idx]
                
#         for key, values in counter.items():
#             if len(values) > 1:
#                 val1 = values[0]
#                 print(key, values)
#                 for idx in range(1, len(values)):
#                     if abs(values[idx] - val1) > k:
#                         return False
#                     val1 = values[idx]
#         return True