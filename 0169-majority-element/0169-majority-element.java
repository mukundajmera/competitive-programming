class Solution {
    public int majorityElement(int[] nums) {
        int majority = 0;
        int number = nums[0];
        for(int num : nums){
            if(majority == 0){
                number = num;
                majority += 1;
            }else if(number == num){
                majority += 1;
            }else{
                majority -= 1;
            }
        }
        return number;        
    }
}