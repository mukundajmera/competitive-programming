class Solution {
    public int[] productExceptSelf(int[] nums) {
        int []answer = new int[nums.length];
        Arrays.fill(answer,1);

        int prev = 1;
        for(int idx=0; idx < answer.length;idx++){
            answer[idx] *= prev;
            prev *= nums[idx];
        }

        prev = 1;
        for(int idx=answer.length-1; idx >= 0;idx--){
            answer[idx] *= prev;
            prev *= nums[idx];
        }

        return answer;

    }
}


        