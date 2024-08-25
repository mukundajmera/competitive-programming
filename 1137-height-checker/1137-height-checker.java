class Solution {
    public int heightChecker(int[] heights) {
        int[] sortedArray = Arrays.copyOf(heights, heights.length);
        Arrays.sort(sortedArray);
        int count = 0;
        for(int idx=0; idx < heights.length; idx++){
            if(heights[idx] != sortedArray[idx]){
                count++;
            }
        }
        return count;
    }
}