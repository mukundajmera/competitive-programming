class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for(int idx = 0;idx < nums.length; idx++){
            int index = Math.abs(nums[idx]) -1;
            if(nums[index] > 0)
            nums[index] = nums[index] * -1;
        }
        
        List<Integer> missingNumber = new ArrayList<>();
        for(int idx = 0;idx < nums.length; idx++){
            if(nums[idx] > 0){
                missingNumber.add(idx+1);                
            }
        }
        return missingNumber;
    }
}