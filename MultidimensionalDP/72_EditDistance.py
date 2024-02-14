class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)+1
        n = len(word2)+1
        dp = [ [0  for j in range(m)] for i in range(n)  ]
        
        for i in range(m):
            dp[0][i] = i
        for i in range(n):
            dp[i][0] = i
        
        for i in range(1, n):
            for j in range(1, m):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],
                                   dp[i-1][j],
                                   dp[i][j-1])+1
        return dp[n-1][m-1]
