class Solution:
     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        n = len(equations)
        
        self.visit = {}
        self.found = False
        def dfs(start, end, ans):
            #print(start, end, ans)
            if start == end:
                #print("found",start, end, ans)
                self.found = True
                return ans
            for e in g[start]:
                if e[0] not in self.visit or self.visit[e[0]] == False:
                    self.visit[e[0]] = True
                    #print("debug",start,  e[0],e[1])
                    tmp = dfs(e[0],end,ans*e[1])
                    if self.found == True:
                        return tmp
                    self.visit[e[0]] = False
            return -1.0
        for i in range(n):
            a = equations[i][0]
            b = equations[i][1]
            g[a].append([b, values[i]])
            g[b].append([a, 1/values[i]] )
        #print(g)
        ans = []
        for q in queries:
            start = q[0]
            end = q[1]
            self.visit = {}
            self.found = False
            if start not in g or end not in g:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, 1))

        return ans

        