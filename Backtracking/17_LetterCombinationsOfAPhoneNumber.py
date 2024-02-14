class Solution(object):
    target_len = -1
    res = []
    def dfs(self,datas,n,c):
        if n ==self.target_len:
            #print c
            self.res.append(c)
            return
        for ch in datas[n]:
           self.dfs(datas,n+1,c+ch)
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.res = []
        map_str = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        datas  = [map_str[int(x)]  for x in digits]
        print datas
        self.target_len = len(digits)
        self.dfs(datas,0,'')
        return self.res