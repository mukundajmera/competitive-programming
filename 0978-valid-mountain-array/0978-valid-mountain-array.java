class Solution {
    public boolean validMountainArray(int[] arr) {
        int len = arr.length, index = 0;
        while(index + 1 < len && arr[index] < arr[index+1]){
            index++;
        }
        // System.out.println(index);
        if(index == 0 || index == len -1){
            return false;
        }

        while(index+1 < len && arr[index] > arr[index+1]){
            index++;
        }

        return index == len-1;
    }
}