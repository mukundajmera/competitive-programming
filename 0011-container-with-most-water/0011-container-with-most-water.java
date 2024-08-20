class Solution {
    public int maxArea(int[] height) {
        int maxWater = 0;
        int leftIdx = 0, rightIdx = height.length-1;

        while(leftIdx < rightIdx){
            int width = rightIdx -  leftIdx;
            int current_height = Math.min(height[leftIdx], height[rightIdx]);
            maxWater = Math.max(maxWater, current_height * width);

            while(leftIdx < rightIdx && height[leftIdx] <= current_height){
                leftIdx++;
            }

            while(leftIdx < rightIdx && height[rightIdx] <= current_height){
                rightIdx--;
            }
        }
        return maxWater;
    }
    // public int maxArea(int[] height) {
    //     int maxWater = 0;
    //     int leftIdx = 0, rightIdx = height.length-1;

    //     while(leftIdx < rightIdx){
    //         int width = rightIdx -  leftIdx;
    //         int current_height = Math.min(height[leftIdx], height[rightIdx]);
    //         maxWater = Math.max(maxWater, current_height * width);

    //         if(height[leftIdx] < height[rightIdx]){
    //             leftIdx++;
    //         }else{
    //             rightIdx--;
    //         }
    //     }
    //     return maxWater;
    // }
}