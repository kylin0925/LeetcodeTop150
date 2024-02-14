class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        tmp = []
        def dfs(p,s,l):
            if l == k:
                ans.append(p[:])
            for i in range(s,n+1):                
                p.append(i)
                dfs(p,i+1,l+1)
                p.pop()                   
        
        dfs(tmp,1,0)
        return ans
        