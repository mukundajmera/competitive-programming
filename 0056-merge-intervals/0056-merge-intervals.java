class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> result = new ArrayList<>();

        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

        for(int[] interval: intervals){
            if(result.isEmpty() || result.get(result.size()-1)[1] < interval[0]){
                result.add(interval);
            }else{
                //merge the intervals
                int[] oldInterval = result.get(result.size()-1);
                oldInterval[0] = Math.min(oldInterval[0], interval[0]);
                oldInterval[1] = Math.max(oldInterval[1], interval[1]);
                // System.out.println(oldInterval[0] + " " + oldInterval[1]);
                result.set(result.size()-1, oldInterval);
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}