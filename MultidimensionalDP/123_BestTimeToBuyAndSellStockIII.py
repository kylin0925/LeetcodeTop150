class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_price = len(prices)
        #dp = [[0 for j in range(num_price + 1)] for i in range(3)]

        p1 = -prices[0]
        p2 = -prices[0]
        
        dp0 =0
        dp1 = 0
        dp2 = 0
        j=1
        print(dp1,dp2,p1,p2)
        while j < num_price:
            #for i in range(1, 3):
            dp1 = max(dp1, prices[j] + p1 )
            p1 = max( p1, -prices[j] )
            
            dp2 = max(dp2, prices[j] + p2 )
            p2  = max(p2, dp1 -prices[j] )
            j+=1
            print(dp1,dp2,p1,p2)
        return dp2