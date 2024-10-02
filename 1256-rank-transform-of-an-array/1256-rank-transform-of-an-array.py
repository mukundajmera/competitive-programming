class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_set = sorted(set(arr))
        element_map = {ele:rank+1 for rank,ele in enumerate(sorted_set)}
        return [element_map[ele] for ele in arr]

        # # Store the rank for each number in arr
        # num_to_indices = {k: [] for k in sorted(set(arr))}

        # for i, num in enumerate(arr):
        #     num_to_indices[num].append(i)

        # rank = 1
        # for num in num_to_indices.keys():
        #     for index in num_to_indices[num]:
        #         arr[index] = rank
        #     rank += 1

        # return arr

        # num_to_rank = {}
        # sorted_arr = sorted(arr)
        # rank = 1
        # for i in range(len(sorted_arr)):
        #     if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
        #         rank += 1
        #     num_to_rank[sorted_arr[i]] = rank
        # for i in range(len(arr)):
        #     arr[i] = num_to_rank[arr[i]]
        # return arr