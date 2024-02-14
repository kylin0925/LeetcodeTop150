class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """   
        table = {}
        if n == 1:
            return True
        tmp = n
        while tmp!=1:
            #print tmp
            tmp = sum( [int(c)**2 for c in str(tmp)])
            if table.has_key(tmp) == True:
               return False
            table[tmp] = 1
        return True 