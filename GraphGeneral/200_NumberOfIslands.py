class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[0,-1],[1,0],[0,1],[-1,0]]
        w = len(grid[0])
        h = len(grid)    
        def dfs(x,y):
            grid[y][x] ='0'
            for direct in d:
                if 0<=x+direct[0]<w and 0<= y+direct[1] < h:
                    if grid[y+direct[1]][x+direct[0]] == '1':
                        dfs(x+direct[0],y+direct[1])
        count = 0
        for y in range(h):
             for x in range(w):
                if grid[y][x] == '1':
                    count+=1
                    dfs(x,y)
        return count
        