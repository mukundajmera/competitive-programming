class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> stack = new ArrayList<>();
        backtrack(nums, 0, stack);
        return stack;
    }

    private void backtrack(int [] nums, int index, List<List<Integer>> stack){
        //base case
        if(index == nums.length){
            List<Integer> currentPermutation = new ArrayList<>();
            for (int num : nums) {
                currentPermutation.add(num);
            }
            stack.add(currentPermutation);
            return;
        }

        for(int idx = index; idx < nums.length; idx++){
            swap(nums, index, idx);
            backtrack(nums, index + 1, stack);
            swap(nums, index, idx);            
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
    }

}