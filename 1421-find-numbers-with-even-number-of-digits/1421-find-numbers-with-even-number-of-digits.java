class Solution {
    public int findNumbers(int[] nums) {
        int total_even = 0;
        for(int num: nums){
            int count = 0;

            while(num > 0){
                num /= 10;
                count++;
            }

            if(count % 2 == 0){
                total_even++;
            }
        }
        return total_even;
    }
}