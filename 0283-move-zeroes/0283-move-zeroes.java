class Solution {
    public void moveZeroes(int[] nums) {
        int index = 0;
        for(int num :nums){
            if(num != 0){
                nums[index++] = num;
            }
        }
        //filling
        while(index < nums.length){
            nums[index++] = 0;
        }
    }

}

/*
    //     //using 2 pointer approach
    //     int left = 0;
    //     int right = nums.length-1;
    //     while(left < right){
    //         while(left < nums.length && nums[left] != 0){
    //             left += 1;
    //         }
    //         while(right >= 0 && nums[right] == 0){
    //             right -= 1;
    //         }
    //         int temp = nums[left];
    //         nums[left] = nums[right];
    //         nums[right] = temp;
    //         left += 1;
    //         right -= 1;            
    //     }
    // }
*/