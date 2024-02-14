class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        #print("g",graph,indegree)
        for cp in prerequisites:
            cour = cp[0]
            pre = cp[1]
            graph[pre].append(cour)
            indegree[cour]+=1
        
        #print(graph)
        #print(indegree)
        q = deque()
        visit = [0] * numCourses
        ans = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        #print("init",q)
        while len(q) > 0:
            i = q.popleft()
            visit[i] = 1
            ans.append(i)
            #print(ans,i)
            for n in graph[i]:
                indegree[n]-=1                
                if indegree[n] == 0:
                    #ans.append(n)
                    q.append(n)
        #print(ans)
        return ans if len(ans) == numCourses else []