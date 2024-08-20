class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
     List<List<Integer>> result = new ArrayList<>();
     dfs(candidates, target, new ArrayList<>(), result, 0);
     return result;
    }

    void dfs(int[] candidates, int target, List<Integer> stack, List<List<Integer>> result, int index) {
        //base case
        if(target < 0){
            return;
        }else if(target == 0){
            result.add(new ArrayList<>(stack));
            return;
        }

        for(int idx = index; idx < candidates.length; idx++){
            stack.add(candidates[idx]);
            dfs(candidates, target - candidates[idx], stack, result, idx);
            stack.remove(stack.size() - 1);
        }
    }
}