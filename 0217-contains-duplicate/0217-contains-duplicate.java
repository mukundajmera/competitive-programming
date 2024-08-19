class Solution {
    public boolean containsDuplicate(int[] nums) {
        //using hashset approach
        Set<Integer> set = new HashSet<>();
        boolean isDup = false;
        for(int num: nums){
            if(set.contains(num)){
                isDup = true;
                break;
            }else{
                set.add(num);
            }
        }
        return isDup;
    }
}