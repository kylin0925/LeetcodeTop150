class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [-1 for i in range(len(s)) ]

        def dfs(i, catstr):
            
            if catstr == s:
                return True
            if i > len(s):
                return False
            r=False
            if memo[i]!=-1:
                return memo[i]
            
            for w in wordDict:
                if s[i:len(w) + i] == w:
                    r |= dfs(i + len(w), catstr + w)

            memo[i] = r
            return r

        ans = dfs(0,"")

        return ans