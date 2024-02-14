class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        count = len(t)

        tmap =dict.fromkeys(list(t), 0)
        for c in t:
            tmap[c] += 1


        #print(tmap,count)
        minsize = 1000000

        R = 0
        L = 0
        ansR = R
        ansL = L


        while R<slen:
            #print(L, R,tmap,s[R])
            if s[R] in tmap:
                if tmap[s[R]] > 0:
                    count-=1
                tmap[s[R]] -= 1

            #print("count",count)
            while count == 0:
                if R-L+1 < minsize:
                    minsize = R-L+1
                    ansR=R
                    ansL=L
                    #print("update min",L,R,minsize)
                if s[L] in tmap:
                    tmap[s[L]]+=1
                    if tmap[s[L]] >0:
                        count+=1
                L += 1
                #print("move L", L,count)
            R += 1
        #print("ans",ansL,ansR)
        return s[ansL:ansR+1] if minsize!=1000000 else ""