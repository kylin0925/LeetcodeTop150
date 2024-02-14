class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix) + 1
        n = len(matrix[0]) +1
        dp = [[0 for i in range(n)] for j in range(m)]
        print(dp)
        area = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
                    area = max(area, dp[i][j] * dp[i][j])
        return area