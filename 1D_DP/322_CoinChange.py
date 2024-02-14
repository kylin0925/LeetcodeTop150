class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins.sort()
        self.min_coin = 0
        lenc = len(coins)

        dp = [amount+1 for i in range(amount + 1)]

        dp[0] = 0
        for i in range(lenc):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    tmp = j - coins[i]
                    c2 = dp[tmp]
                    #print(c1,c2)
                    dp[j] = min(c2 +1 ,dp[j])
                #print(coins[i], j, dp)
        #print(dp)
        return dp[amount] if dp[amount] != amount +1 else -1