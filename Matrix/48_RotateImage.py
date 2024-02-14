class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(n-i-1):
                swidx = n-j-1 -i
                #print(swidx)
                matrix[i][j],matrix[i + swidx][j+ swidx] = matrix[i + swidx][j+ swidx],matrix[i][j]
            #print(i,matrix)
        #print(matrix)
        #swap upside down mirror
        for i in range(n//2):
            offy = n - i - 1
            for j in range(n):
                matrix[i][j], matrix[offy][j] = matrix[offy][j], matrix[i][j]

        #print(matrix)