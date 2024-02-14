class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        n = len(strs[0])
        
        while i < n:
            c = strs[0][i]
            for s in strs:                
                if i >= len(s) or s[i]!=c:
                    return strs[0][0:i]                               
            i+=1

        return strs[0][0:i] 