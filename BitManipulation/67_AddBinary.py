class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a) - 1
        lenb = len(b) - 1
        c = 0
        ans = ""
        while lena >= 0 or lenb >=0:
            if lena >=0:
                na = int(a[lena])
                lena-=1
            if lenb >=0:
                nb = int(b[lenb])
                lenb-=1

            tmp = (na+nb+c)%2
            c = (na+nb+c)//2
            na=nb=0
            ans += str(tmp)
        if c > 0:
            ans +="1"    
        return ans[::-1]
