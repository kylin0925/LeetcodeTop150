class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len (profits)
        projects=[]
        for i in range(n):
            projects.append([capital[i], profits[i]])
        projects.sort()
        #print(projects)
        i = 0
        hq = []
        while k>0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(hq, -projects[i][1])
                i+=1
            if len(hq) == 0:
                break
            t = -heapq.heappop(hq)
            w+=t
            k-=1
        return w
        