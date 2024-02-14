class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        if len(points) == 1:
            return 1
        for p in points:
            tbl ={}
            ver = 1
            for p2 in points:
                
                if p[0]==p2[0] and p[1]==p2[1]:
                    continue
                if p[0]==p2[0]:
                    ver+=1 
                else:
                    dx = p2[0] - p[0]
                    dy = p2[1] - p[1]
                    slop = dy/dx
                    if slop in tbl:
                        tbl[slop]+=1
                    else:
                        tbl[slop]=2
                        
                    ans = max(ans,tbl[slop])
            ans = max(ans,ver)
            
                
        return ans