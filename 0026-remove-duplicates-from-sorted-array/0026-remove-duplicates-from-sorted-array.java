class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;
        for(int i = 1; i < nums.length;i++){
            if(nums[i] != nums[i-1]){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
        // int index = 0;
        // Set<Integer> visited = new HashSet<>();
        // for(int i = 0; i < nums.length;i++){
        //     if(!visited.contains(nums[i])){
        //         visited.add(nums[i]);
        //         nums[index] = nums[i];
        //         index++;
        //     }
        // }
        // return index;
    }
}