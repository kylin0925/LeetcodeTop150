class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt_5 = 0
        
        while n > 0:
            cnt_5 += n/5
            n=n/5
        return cnt_5