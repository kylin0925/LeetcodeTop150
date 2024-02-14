class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(board,x,y,c):
            cnt = 0
            m = len(board)
            n = len(board[0])
            
            if x-1 >=0 and y-1>=0:
                if board[y-1][x-1] == c:
                    cnt+=1
            
            if y-1>=0:
                if board[y-1][x] == c:
                    cnt+=1
            
            if x+1 <n and y-1>=0:
                if board[y-1][x+1] == c:
                    cnt+=1
            
            if x-1 >=0 :
                if board[y][x-1] == c:
                    cnt+=1
                    
            if x+1 < n:
                if board[y][x+1] == c:
                    cnt+=1
                    
            if x-1 >=0 and y+1<m:
                if board[y+1][x-1] == c:
                    cnt+=1
                    
            if y+1<m:
                if board[y+1][x] == c:
                    cnt+=1
                    
            if x+1 < n and y+1 < m:
                if board[y+1][x+1] == c:
                    cnt+=1
                    
            return cnt

        m = len(board)
        n = len(board[0])
        tmp_board = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cnt = count(board,j,i,1)
                #print(i,j,cnt)
                if board[i][j] == 1:
                    if cnt < 2:
                        tmp_board[i][j] = 0
                    elif cnt ==2 or cnt == 3:
                        tmp_board[i][j] = 1
                    elif cnt>3:
                        tmp_board[i][j] = 0
                else:
                    if cnt == 3:
                        tmp_board[i][j] = 1
        #print(tmp_board)
        for i in range(m):
            board[i] = tmp_board[i][:]