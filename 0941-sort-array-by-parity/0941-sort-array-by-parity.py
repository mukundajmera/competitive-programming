class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums)-1
        while even < odd:
            if nums[even] % 2 != 0:
                # replace with even from odd until we fine odd
                while even < odd:
                    if nums[odd] % 2 != 0:
                        odd -= 1
                    else:
                        break;
                #swap number
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1
            else:
                even += 1
        return nums
        
        