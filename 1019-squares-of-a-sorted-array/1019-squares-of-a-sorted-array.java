class Solution {
    public int[] sortedSquares(int[] nums) {
        for(int idx = 0;idx <  nums.length; idx++){
            nums[idx] *= nums[idx];
        }
        Arrays.sort(nums);
        return nums;
    }
}