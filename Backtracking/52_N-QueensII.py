class Solution:
    def totalNQueens(self, n: int) -> int:
        chkh = [0 for i in range(n)]
        chkld = [0 for i in range(2*n)]
        chkrd = [0 for i in range(2*n)]
        nq = [['.' for i in range(n)] for i in range(n)]
        #ans_nq=[]
        self.cnt = 0
        def dfs(i):

            if i == n:
                #print(nq)
                #tmp = []
                #for row in nq:
                #    tmp.append("".join(row[:]))
                #ans_nq.append(tmp)
                self.cnt +=1
                return
            for j in range(n):
                if chkh[j] == 0 and chkld[i-j + n] == 0 and chkrd[i+j] ==0:
                    nq[i][j] = 'Q'
                    chkh[j] = 1
                    chkld[i - j + n] = 1
                    chkrd[i + j] = 1
                    dfs(i+1)
                    nq[i][j] = '.'
                    chkh[j] = 0
                    chkld[i - j + n] = 0
                    chkrd[i + j] = 0
                #print(j)

        dfs(0)
        #print(self.cnt,ans_nq)
        return self.cnt