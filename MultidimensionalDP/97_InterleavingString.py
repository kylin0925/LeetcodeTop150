class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.found = False
        tbl = {}
        if len(s1) + len(s2) != len(s3):
            return False
        
        def dfs(i,j,tmptarget):
            #print(i,j,tmptarget)

            if i+j == len(s3):
                #print(i, j, tmptarget,tmptarget == s3)
                if tmptarget == s3:
                    self.found=True
                    return
            if tmptarget!="" and tmptarget[-1] != s3[i+j-1]:
                #print("return")
                return

            if tbl.get((i,j))!=None:
                return tbl[(i,j)]
            if self.found==False and i<len(s1):
                dfs(i+1,j,tmptarget+s1[i])

            if self.found==False and j<len(s2):
                dfs(i,j+1,tmptarget+s2[j])

            if tbl.get((i,j))==None:
                tbl[(i,j)] =self.found
            #else:
            #    print("cached ",tbl[(i,j)])
        dfs(0,0,"")

        return self.found