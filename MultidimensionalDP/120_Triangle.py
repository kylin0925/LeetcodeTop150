class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        dp = [ triangle[-1][i] for i in range(depth)]       
        for y in range(depth-2,-1,-1):
            for x in range(y+1):
                dp[x] = min(triangle[y][x] + dp[x], triangle[y][x] + dp[x+1])
            
        return dp[0]