class Solution {
    public void duplicateZeros(int[] arr) {
        //2 passs
        int possibleDuplicate = 0;
        int len = arr.length-1;
        for(int index = 0; index <= len - possibleDuplicate; index++){
            if(arr[index] == 0){
                if(index == len - possibleDuplicate){
                    arr[len] = 0;
                    len -= 1;
                    break;
                }
                possibleDuplicate++;
            }
        }

        int last = len - possibleDuplicate;
        for(int index = last; index >= 0; index-- ){
            if(arr[index] == 0){
                arr[index + possibleDuplicate] = 0;
                possibleDuplicate--;
                arr[index + possibleDuplicate] = 0;
            }else{
                arr[index + possibleDuplicate] = arr[index];
            }
        }
    }
}