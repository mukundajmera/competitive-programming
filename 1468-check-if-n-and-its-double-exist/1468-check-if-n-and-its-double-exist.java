class Solution {
    public boolean checkIfExist(int[] arr) {
        //using hashset approach
        Set<Integer> seen = new HashSet<>();
        boolean exist = false;
        for(int num: arr){
            if((num % 2 == 0 &&seen.contains(num/2)) || seen.contains(num*2)){
                // System.out.println(num + " " + num/2);
                exist = true;
                break;
            }
            seen.add(num);
        }
        return exist;
        
    }
}