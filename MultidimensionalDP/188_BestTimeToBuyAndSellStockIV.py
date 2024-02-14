class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int: 
        if len(prices) == 0:
            return 0
        num_price= len(prices)
        dp = [ [0 for j in range(num_price+1)] for i in range(k+1) ]


        for i in range(1,k+1):
            minp = -prices[0]
            
            for j in range(1,num_price):                
                dp[i][j] = max(dp[i][j-1],prices[j] + minp )
                minp = max(minp, dp[i-1][j-1] -prices[j] )
                                
        #print(dp)
        return dp[k][num_price-1]
