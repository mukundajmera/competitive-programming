class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int len = intervals.length, idx = 0;
        List<int[]> result = new ArrayList<>();

        while(idx < len && intervals[idx][1] < newInterval[0]){
            result.add(intervals[idx++]);
        }

        //breaking condition for merging intervals
        while(idx < len && newInterval[1] >= intervals[idx][0]){
            newInterval[0] = Math.min(newInterval[0], intervals[idx][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[idx][1]);
            idx++;            
        }
        result.add(newInterval);
        while(idx < len){
            result.add(intervals[idx++]);
        }
        return result.toArray(new int[result.size()][]);
    }
}