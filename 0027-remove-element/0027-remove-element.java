class Solution {
    public int removeElement(int[] nums, int val) {
        int pointer = 0;
        for(int index = 0; index < nums.length; index++){
            if(nums[index] != val){
                nums[pointer] = nums[index];
                pointer++;
            }
        }
        return pointer;
        // int left = 0;
        // int right = nums.length -1;
        // int count = 0;
        // while(left < right){
        //     while(left < right && nums[left] != val){
        //         left++;
        //         count++;
        //     }
        //     while(left < right && nums[right] == val){
        //         right--;
        //     }
        //     int temp = nums[left];
        //     nums[left] = nums[right];
        //     nums[right] = temp;
        // }
        // return count;
    }
}