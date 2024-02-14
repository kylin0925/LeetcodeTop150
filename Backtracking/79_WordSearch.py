class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        flag = [[False for i in range(n)] for j in range(m)]
        self.f = False
        def dfs(i,j,idx):
            if self.f:
                return
            if idx == len(word):
                self.f=True
                return
            
            if i-1 >= 0:
                if board[i-1][j] == word[idx] and flag[i-1][j]==False:
                    flag[i-1][j]=True
                    dfs(i-1,j,idx+1)
                    flag[i-1][j]=False
                    
            if i+1 < m:
                if board[i+1][j] == word[idx] and flag[i+1][j]==False:
                    flag[i+1][j]=True
                    dfs(i+1,j,idx+1)
                    flag[i+1][j]=False
                    
            if j-1 >= 0:
                if board[i][j-1] == word[idx] and flag[i][j-1]==False:
                    flag[i][j-1]=True
                    dfs(i,j-1,idx+1) 
                    flag[i][j-1]=False
            if j+1 < n:
                if board[i][j+1] == word[idx] and flag[i][j+1]==False:
                    flag[i][j+1]=True
                    dfs(i,j+1,idx+1)
                    flag[i][j+1]=False
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j]=True
                    dfs(i,j,1)
                    flag[i][j]=False
                    
        return self.f
        