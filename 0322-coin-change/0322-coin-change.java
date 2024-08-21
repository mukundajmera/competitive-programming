class Solution {
    public int coinChange(int[] coins, int amount) {
        int []dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for(int idx = 1; idx < amount+1;idx++){
            for(int coin : coins){
                if(idx - coin >= 0){
                    dp[idx] = Math.min(dp[idx], 1 + dp[idx - coin]);
                }
            }
        }        
        if(dp[amount] != amount + 1){
            return dp[amount];
        }
        return -1;    
    }
}
