class Solution {
    public int[] replaceElements(int[] arr) {
        int currentMax = -1;
        for(int idx = arr.length-1; idx >= 0; idx--){
            int element = arr[idx];
            arr[idx] = currentMax;
            currentMax = Math.max(currentMax, element);
        }
        return arr;
    }
}