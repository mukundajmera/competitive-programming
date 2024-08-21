class Solution {
    public int maxSubArray(int[] nums) {
        int current_max = 0;
        int max_number = Integer.MIN_VALUE;
        for(int num : nums){
            current_max = Math.max(current_max + num, num);
            max_number = Math.max(max_number, current_max);
        }
        return max_number;
    }
}