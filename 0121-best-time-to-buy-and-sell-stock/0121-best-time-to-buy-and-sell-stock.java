class Solution {
    public int maxProfit(int[] prices) {
        //asume buy at zero
        int buyAt = prices[0];
        int maxProfit = Integer.MIN_VALUE;
        for(int index = 0; index < prices.length; index++){
            if(buyAt > prices[index]){
                buyAt = prices[index];
            }
            // System.out.println(buyAt + " " + prices[index]);
            maxProfit = Math.max(maxProfit,  prices[index] - buyAt);
        }
        return maxProfit;
    }
}