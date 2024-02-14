class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        tlen = len(t)
        for c in s:
            j = i
            while j <tlen:
                if c == t[j]:
                    i=j+1
                    break
                j+=1
            print(c,j)
            if j == tlen:
                return False
        return True