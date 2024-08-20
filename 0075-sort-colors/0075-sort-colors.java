class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length-1;
        int zero = 0;
        while(left <= right){
            if(nums[left] == 0){
                int temp = nums[zero];
                nums[zero] = nums[left];
                nums[left] = temp;
                zero++;
                left++;
            }else if(nums[left] == 2){
                //swap the number with right
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                right--;
            }else{
                left++;
            }
        }
    }
}