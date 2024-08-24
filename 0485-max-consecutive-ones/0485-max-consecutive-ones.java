class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_count = 0;
        int count = 0;
        for(int index = 0; index < nums.length; index++){
            if(nums[index] == 0){
                max_count = Math.max(max_count, count);
                count = 0;
            }else{
                count += 1;
            }
        }
        max_count = Math.max(max_count, count);
        return max_count;
            
    }
}