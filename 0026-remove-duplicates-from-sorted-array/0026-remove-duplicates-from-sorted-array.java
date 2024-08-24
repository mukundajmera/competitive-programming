class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        Set<Integer> visited = new HashSet<>();
        for(int i = 0; i < nums.length;i++){
            if(!visited.contains(nums[i])){
                visited.add(nums[i]);
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}