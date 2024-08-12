class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        isLeft = self.binary_search(nums, 0, mid, target)
        if isLeft != -1:
            return isLeft
        return self.binary_search(nums, mid, len(nums)-1, target)
            

    
    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            # print(mid, left, right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     left, right = 0, n - 1

    #     # Find the index of the pivot element (the smallest element)
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] > nums[-1]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     # print(left, right, mid)
    #     # Binary search over an inclusive range [left_boundary ~ right_boundary]
    #     def binarySearch(left_boundary, right_boundary, target):
    #         left, right = left_boundary, right_boundary
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if nums[mid] == target:
    #                 return mid
    #             elif nums[mid] > target:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         return -1
    #     if (answer:= binarySearch(0, left-1, target)) != -1:
    #         return answer
    #     # print( binarySearch(left, n-1, target))
    #     return binarySearch(left, n-1, target)