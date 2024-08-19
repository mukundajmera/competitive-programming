class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> remaining = new HashMap<>();
        for(int index = 0; index < nums.length; index++){
            int diff = target - nums[index];
            if(remaining.containsKey(diff)){
                result[0] = remaining.get(diff);
                result[1] = index;
            }else{
                remaining.put(nums[index], index);
            }
        }
        return result;
    }
}