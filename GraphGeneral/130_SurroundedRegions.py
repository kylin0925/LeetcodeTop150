class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visit = {}
        m = len(board)
        n = len(board[0])
        self.canMark=True
        def dfs(x,y):
            visit[(x,y)]=1
            if x == 0 or y == 0 or x == n-1 or y == m-1:
                self.canMark=False
                        
            if x+1 < n and board[y][x+1] =='O':
                if (x+1,y) not in visit:
                    dfs(x+1,y)
            if x-1>=0 and board[y][x-1]=='O':
                if (x-1,y) not in visit:
                    dfs(x-1,y)                    
            if y+1<m and board[y+1][x]=='O':
                if (x,y+1) not in visit:
                    dfs(x,y+1)
            if y-1>=0 and board[y-1][x]=='O':
                if (x,y-1) not in visit:
                    dfs(x,y-1)                    
            
        def mark():
            for k in visit.keys():
                if visit[k]==1:
                    if self.canMark:
                        board[k[1]][k[0]]='X'
                    visit[k]=2
        for i in range(m):
            for j in range(n):
                if (j,i) not in visit and board[i][j] == 'O':
                    self.canMark=True
                    dfs(j,i)
                    #print(visit)
                    mark()
                        