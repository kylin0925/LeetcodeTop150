class Solution:
    def calculate(self, se: str) -> int:
        s=1
        r=0
        tmp = 0
        stack = []
        for c in se:
            if c.isdigit():
                tmp =tmp*10 + int(c)
            elif c == "+":
                r = r + s*tmp
                tmp=0
                s=1
            elif c == "-":
                r = r + s*tmp
                tmp=0
                s=-1
            elif c == "(":
                stack.append((r,s))
                r=0
                s=1
            elif c == ")":
                r = r + s*tmp                
                sr,ss = stack.pop()
                r= sr+ ss* r 
                s=1
                tmp=0
            #print(c,r,tmp,stack)
        if tmp !=0:
            r+= s*tmp
            tmp=0
        #print(r,tmp,stack)
        return r
        