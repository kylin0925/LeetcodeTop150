class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxSum = 0
        for row in grid:
            maxSum += sum(row)

        maxSum+=1
        m = len(grid)
        n = len(grid[0])

        sumMap = [[maxSum for x in range(n)] for y in range(m) ]
        for i in range(m):
            for j in range(n):
                tmp =0
                if i ==0 and j ==0:
                    sumMap[i][j] = grid[i][j]
                    continue
                up = maxSum
                left = maxSum
                if i - 1 >=0:
                    up =grid[i][j]+sumMap[i-1][j]
                if j - 1 >=0:
                    left =grid[i][j] + sumMap[i][j-1]
                sumMap[i][j] = min(up,left)
        #print(sumMap)
        return sumMap[m-1][n-1]