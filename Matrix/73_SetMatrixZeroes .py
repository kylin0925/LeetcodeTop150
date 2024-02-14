class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowToZero = False
        colToZero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    if j==0:
                        colToZero=True
                    if i==0:
                        rowToZero=True
        #print(matrix)                        
        for i in range(1,m):            
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        #print(matrix)              
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0                    
        #print(matrix)  
        if rowToZero==True:
            for i in range(n):
                matrix[0][i] = 0
        if colToZero==True:
            for i in range(m):
                matrix[i][0] = 0
