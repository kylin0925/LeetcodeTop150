class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direct = [[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1]]
        xy_offset = [[-1, 1],
                     [-1, -1],
                     [1, -1],
                     [1, 1]]

        dir = 0
        res = []

        x=y=0
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        total = 0
        flag_map = [[0 for i in range(n)] for j in range(m)]
        while total < m*n:

            if dir == 0:
                if x>=n or flag_map[y][x] == -1:
                    x+=xy_offset[dir][0]
                    y+=xy_offset[dir][1]
                    dir+=1
            elif dir == 1:
                if y>=m or flag_map[y][x] == -1:
                    x+=xy_offset[dir][0]
                    y+=xy_offset[dir][1]
                    dir+=1
            elif dir == 2:
                if  x<0 or flag_map[y][x] == -1:
                    x+=xy_offset[dir][0]
                    y+=xy_offset[dir][1]
                    dir+=1
            elif dir == 3:
                if y<0 or flag_map[y][x] == -1:
                    x+=xy_offset[dir][0]
                    y+=xy_offset[dir][1]
                    dir=0
            #print(dir, x, y)
            res.append(matrix[y][x])
            flag_map[y][x] = -1
            total += 1
            x += direct[dir][0]
            y += direct[dir][1]

        #print(res)
        return res