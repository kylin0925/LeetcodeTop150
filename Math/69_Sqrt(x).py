class Solution:
    def mySqrt(self, x: int) -> int:
        p = 0
        while (p+1)*(p+1) <= x:
                p+=1

        return p
