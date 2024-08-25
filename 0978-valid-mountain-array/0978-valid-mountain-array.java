class Solution {
    public boolean validMountainArray(int[] arr) {
        /*
                N = len(arr)
        i = 0

        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == N-1:
            return False

        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
        */
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