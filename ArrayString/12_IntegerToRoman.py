symbol = [  ["","I","II","III","IV","V","VI","VII","VIII","IX"],
            ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
            ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
            ["","M","MM","MMM"]]
            
class Solution(object):
    def intToRoman(self, n):
        """
        :type s: str
        :rtype: int
        """
        s = str(n)
        l = len(s)
        i = 0;
        res = "";
        while i < l:
            p = s[i]  
            res += symbol[l-i-1][int(p)]
            i+=1
        return res    