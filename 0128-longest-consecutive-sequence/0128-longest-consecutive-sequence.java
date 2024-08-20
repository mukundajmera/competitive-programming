class Solution {
    public int longestConsecutive(int[] nums) {
        //sorted and check previous nlogn
        //use hashmap checking previous element if exists
        int maxSeq = 0;
        Map<Integer,Integer> numMap = new HashMap<>();
        for(int num =0; num < nums.length; num++){
            numMap.put(nums[num], num);
        }
        for(int num =0; num < nums.length; num++){
            if(numMap.get(nums[num]-1) == null){
                int  count = 0;
                int currentNum = nums[num];
                while(numMap.get(currentNum + count) != null ){
                    count++;
                }
                maxSeq = Math.max(maxSeq, count);
                // System.out.println(currentNum + " " + count + " " + maxSeq);
            }            
        }
        return maxSeq;
    }
}