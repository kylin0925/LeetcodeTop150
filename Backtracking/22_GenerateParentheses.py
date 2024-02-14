class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        data = []
        def verify(text):
            stack = []
            for c in text:
                if c == "(":
                    stack.append(c)
                else:
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop(len(stack)-1)
                    else:
                        return False
            return True if len(stack) == 0 else False
        def dfs(lv,n,data,p):
            ps = ["(",")"]
            #print(lv,n)
            if lv == (n-1)*2:
                #print("data",data)
                if data.count("(") == data.count(")"):
                    tmp = "(" + "".join(data) + ")"
                    if verify(tmp):
                        res.append(tmp)
                return

            tmp = "("
            data.append("(")

            dfs(lv+1,n,data,tmp)
            tmp = ")"
            data[-1] = tmp
            dfs(lv + 1, n, data, tmp)
            data.pop(lv)
        dfs(0,n,data,"(")
        #print(res,len(res))
        return res