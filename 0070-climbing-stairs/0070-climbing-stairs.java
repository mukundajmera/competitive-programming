class Solution {
    public int climbStairs(int n) {
        if(n == 1){
            return 1;
        }
        int []dp = new int[n+1];
        Arrays.fill(dp, 0);
        dp[1] = 1;
        dp[2] = 2;
        for(int idx = 3; idx < n+1;idx++){
            dp[idx] = dp[idx-2] + dp[idx-1];
        }
        return dp[n];
    }
}