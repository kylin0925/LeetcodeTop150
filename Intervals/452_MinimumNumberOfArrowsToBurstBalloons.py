class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0],-x[1]))
        #print(points)
        n = len(points)

        cnt = 1
        start = points[0] 
        for i in range(1, n):
            x = points[i][0]
            y = points[i][1]
            if start[0] <= x <= start[1] :
                start[0] = max(start[0], x)
                start[1] = min(start[1], y)
            else:
                start = points[i]
                cnt+=1
        return cnt