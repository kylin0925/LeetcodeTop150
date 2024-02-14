class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def listToNumList(tolist):
            strlist = []
            strdict = {}
            i = 0
            for c in tolist:
                n = strdict.get(c) 
                if n == None:
                    strdict[c] = i
                    strlist.append(i)
                    i+=1
                else:
                    strlist.append(n)
            
            #print(strlist,strdict)
            return strlist
        
        plen = len(pattern)
        slist = s.split()
        slen = len(slist)
        
        if plen != slen:
            return False
        
        
        
        p = listToNumList(list(pattern))
        sp = listToNumList(slist)
        print(p,sp)
        return p == sp
                          