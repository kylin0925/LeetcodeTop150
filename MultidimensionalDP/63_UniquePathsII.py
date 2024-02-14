class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        pathMap = [[0 for x in range(n)] for y in range(m)]


        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i-1 >= 0 and obstacleGrid[i-1][j] ==0:
                    pathMap[i][j] += pathMap[i-1][j]
                if j-1>=0 and obstacleGrid[i][j-1] == 0:
                    pathMap[i][j]+=pathMap[i][j-1]
                if i ==0 and j==0:
                    pathMap[i][j] = 1

        print(pathMap)
        return pathMap[m-1][n-1]