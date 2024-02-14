class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # bin search in 1st col
        # bin search
        m = len(matrix)
        n = len(matrix[0])
        nums = m*n
        s = 0
        e = m*n-1
        while s<=e:
            mid = (s+e)>>1
            y = mid//n
            x = mid%n
            if matrix[y][x] == target:
                break
            if matrix[y][x] < target:
                s = mid + 1
            else:
                e = mid-1
        #print(s,mid,e)
        y = mid//n
        x = mid%n                
        return matrix[y][x]==target
                
